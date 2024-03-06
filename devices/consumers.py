from devices import context_processors as cp
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.consumer import AsyncConsumer
from asgiref.sync import async_to_sync
from serial import SerialException, Serial
from threading import Thread
import base64
import json
import time

from urllib.parse import urljoin
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from requests.exceptions import ConnectionError, HTTPError, ReadTimeout, ChunkedEncodingError
import xmltodict

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scalesoft.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from devices.models import Scale, IPCamera

class TruckScaleConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        id = self.scope["url_route"]["kwargs"]["id"]
        if int(id) > 1:  # Number of the maximum devices (truck scale)
            return
        self.group_name = "group_truckscale_" + id
        self.worker_channel_name = "truckscale_" + id
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.channel_layer.send(self.worker_channel_name, {"type": "resume", "channel_name": self.channel_name})
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        await self.channel_layer.send(self.worker_channel_name, {"type": "stop", "channel_name": self.channel_name})

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        if type(data) is not dict:
            await self.send(text_data=json.dumps({"ok": False, "message": "Invalid message"}))
        elif data.get("method"):
            if data['method'] == 'GET':
                pass
            elif data['method'] == 'POST':
                try:
                    pk = int(data.get('pk'))
                except:
                    pk = 0
                if pk:
                    try:
                        obj = Scale.objects.get(pk=pk)
                        cp.update_data(self.worker_channel_name, pk)
                        await self.channel_layer.send(self.worker_channel_name, {"type": "start",
                                                                                 "group_name": self.group_name,
                                                                                 "channel_name": self.channel_name,
                                                                                 "comport": obj.port,
                                                                                 "protocol": obj.protocol.name})
                    except Scale.DoesNotExist:
                        await self.send(text_data=json.dumps({"ok": False, "message": "Invalid pk"}))
                else:
                    await self.send(text_data=json.dumps({"ok": False, "message": "Invalid pk"}))
            elif data['method'] == 'DELETE':
                cp.update_data(self.worker_channel_name, 0)
                await self.channel_layer.send(self.worker_channel_name, {"type": "close", "channel_name": self.channel_name})
            else:
                await self.send(text_data=json.dumps({"ok": False, "message": "Wrong method"}))
        else:
            await self.send(text_data=json.dumps({"ok": False, "message": "Keywords not provided"}))

    async def send_message(self, message):
        if message['ok']:
            await self.send(text_data=json.dumps({"ok": True,
                                                  "data": message['data']}))
        else:
            await self.send(text_data=json.dumps({"ok": False,
                                                  "message": message['message']}))


class TruckScaleWorkerConsumer(AsyncConsumer):
    serial_conn = None
    _thread = None
    _read = False
    _channels = set()

    async def start(self, message):
        print("start task...")
        self._channels.add(message['channel_name'])
        self.receiver = message['group_name']
        self.comport = message['comport']
        self.protocol = message['protocol']
        await self.connect_to_scale()
        self._start_main_thread()

    def _start_main_thread(self):
        if self.serial_conn and self.serial_conn.is_open and (self._thread is None or not self._thread.is_alive()):
            self._read = True
            self._thread = Thread(target=async_to_sync(self._send_data))
            self._thread.daemon = True
            self._thread.start()

    async def stop(self, message):
        print("stop scale...")
        self._channels.discard(message['channel_name'])
        if len(self._channels) == 0:
            self._read = False

    async def resume(self, message):
        print("resume scale...")
        self._channels.add(message['channel_name'])
        self._start_main_thread()

    async def close(self, message=None):
        print("close scale ...")
        if self.serial_conn:
            self.serial_conn.close()
        await self.channel_layer.group_send(self.receiver,
                                            {'type': 'send_message',
                                                     'ok': False,
                                                     'message': "Connection to device lost"})

    async def _send_data(self):
        while self._read:
            await self.send_message()
        print("stopped scale thread")

    async def send_message(self):
        if self.serial_conn.is_open:
            await self.read_data_from_scale()
            await self.channel_layer.group_send(self.receiver,
                                                {'type': 'send_message',
                                                 'ok': True,
                                                 'data': self._weight})
        else:
            self._read = False
            await self.close()

    async def connect_to_scale(self):
        try:
            if self.serial_conn and self.serial_conn.is_open:
                self.serial_conn.close()
            self.serial_conn = Serial(self.comport)
            await self.read_data_from_scale()
        except SerialException as ex:
            await self.close()

    async def read_data_from_scale(self):
        self._reset = True
        try:
            if self._reset:
                self.serial_conn.reset_input_buffer()

            SOF = "02"
            EOF = "03"
            # FIND START OF FRAME
            while self.serial_conn.read().hex() != SOF:
                continue
            # RECORD UNTIL END OF FRAME
            data = bytes()
            while True:
                temp = self.serial_conn.read()
                if temp.hex() == EOF:
                    break
                else:
                    data += temp
            self._weight = self.get_weight(data.decode("utf-8"))
        except SerialException:
            self.serial_conn.is_open = False
            await self.close()

    def get_weight(self, data):
        self.protocol = "A9"
        try:
            if self.protocol == "A9":
                decimal = int(data[7])
                return str(round(int(data[:7]) * 10**(-decimal), decimal))
            else:
                return data
        except:
            return "0"


class IPCameraConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        id = self.scope["url_route"]["kwargs"]["id"]
        if int(id) > 2:  # Number of the maximum devices (ip camera)
            return
        self.group_name = "group_ipcamera_" + id
        self.worker_channel_name = "ipcamera_" + id
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.channel_layer.send(self.worker_channel_name, {"type": "resume", "channel_name": self.channel_name})
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        await self.channel_layer.send(self.worker_channel_name, {"type": "stop", "channel_name": self.channel_name})

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        if type(data) is not dict:
            await self.send(text_data=json.dumps({"ok": False, "message": "Invalid message"}))
        elif data.get("method"):
            if data['method'] == 'GET':
                pass
            elif data['method'] == 'POST':
                try:
                    pk = int(data.get('pk'))
                except:
                    pk = 0
                if pk:
                    try:
                        obj = IPCamera.objects.get(pk=pk)
                        self.scope['session'][self.worker_channel_name] = pk
                        cp.update_data(self.worker_channel_name, pk)
                        await self.channel_layer.send(self.worker_channel_name, {"type": "start",
                                                                                 "group_name": self.group_name,
                                                                                 "channel_name": self.channel_name,
                                                                                 "ipcam": obj.ip_address,
                                                                                 "username": obj.username,
                                                                                 "password": obj.password,
                                                                                 "anpr": obj.anpr})
                    except Scale.DoesNotExist:
                        await self.send(text_data=json.dumps({"ok": False, "message": "Invalid pk"}))
                else:
                    await self.send(text_data=json.dumps({"ok": False, "message": "Invalid pk"}))
            elif data['method'] == 'DELETE':
                cp.update_data(self.worker_channel_name, 0)
                await self.channel_layer.send(self.worker_channel_name, {"type": "close", "channel_name": self.channel_name})
            else:
                await self.send(text_data=json.dumps({"ok": False, "message": "Wrong method"}))
        else:
            await self.send(text_data=json.dumps({"ok": False, "message": "Keywords not provided"}))

    async def send_message(self, message):
        if message.get('ok'):
            if message.get('image_b64'):
                await self.send(text_data=json.dumps({"ok": True,
                                                      "image_b64": message['image_b64']}))
            else:
                await self.send(text_data=json.dumps({"ok": True,
                                                      "data": message['data']}))
        else:
            await self.send(text_data=json.dumps({"ok": False,
                                                  "message": message['message']}))


class IPCameraWorkerConsumer(AsyncConsumer):
    _thread = None
    _channels = set()
    hikapi = None
    ipcam = None
    username = None
    password = None
    anpr = False

    async def start(self, message):
        print("task started")
        self._channels.add(message['channel_name'])
        self.receiver = message['group_name']
        self.ipcam = message['ipcam']
        self.username = message['username']
        self.password = message['password']
        self.anpr = message['anpr']
        await self.connect_hikapi()
        self._start_main_thread()

    def _start_main_thread(self):
        if self.hikapi and self.hikapi.is_open and (self._thread is None or not self._thread.is_alive()):
            self.hikapi.read = True
            thread_pictures = Thread(
                target=self.hikapi.get_pictures, args=())
            thread_pictures.daemon = True
            thread_pictures.start()

            if self.anpr:
                thread_events = Thread(
                    target=self.hikapi.get_events, args=())
                thread_events.daemon = True
                thread_events.start()

            self._thread = Thread(target=async_to_sync(self._send_data))
            self._thread.daemon = True
            self._thread.start()

    async def stop(self, message):
        print("stop task...")
        self._channels.discard(message["channel_name"])
        if len(self._channels) == 0 and self.hikapi:
            self.hikapi.read = False

    async def resume(self, message):
        print("resume camera...")
        self._channels.add(message["channel_name"])
        self._start_main_thread()

    async def close(self, message=None):
        if self.hikapi:
            self.hikapi.is_open = False
            self.hikapi.read = False
        await self.channel_layer.group_send(self.receiver,
                                            {'type': 'send_message',
                                                     'ok': False,
                                                     'message': "Connection to device lost"})

    async def connect_hikapi(self):
        print("try connect...")
        tries = 3
        while tries:
            try:
                self.hikapi = HikvisionAPI(
                    host="http://" + self.ipcam, username=self.username, password=self.password)
                self.hikapi.bg_task = self
                break
            except ReadTimeout:
                tries -= 1
                continue
            except (ConnectionError, HTTPError):
                await self.close()
                break

    async def _send_data(self):
        while self.hikapi.read and self.hikapi.is_open:
            if len(self.hikapi.pictures):
                image_b64 = self.hikapi.pictures.pop(0)
                await self.channel_layer.group_send(self.receiver,
                                                    {'type': 'send_message',
                                                     'ok': True,
                                                     'image_b64': image_b64})
            else:
                time.sleep(0.2)
            if self.anpr and len(self.hikapi.events):
                data = self.hikapi.events.pop(0)
                await self.channel_layer.group_send(self.receiver,
                                                    {'type': 'send_message',
                                                     'ok': True,
                                                     'data': data})
        print("end is_open camera")


class HikvisionAPI:
    image_queue_size = 5
    time_interval_pictures = 0.05
    _spend_time_for_picture = 1  # updated on each request to image

    def __init__(self, host: str, username: str = None, password: str = None):
        """
        :param host: Host for device ('http://192.168.0.2')
        :param username: (optional) username for device
        :param password: (optional) Password for device
        :param timeout: (optional) Timeout for request
        """
        self.host = host
        self.username = username
        self.password = password
        self.session = self.get_session()
        self.is_open = True
        self.read = False
        self.pictures = []
        self.events = []

    def get_session(self):
        """Check the connection with device

         :return request.session() object
        """
        full_url = urljoin(self.host, '/ISAPI/System/status')
        session = requests.session()
        session.auth = HTTPBasicAuth(self.username, self.password)
        response = session.get(full_url)
        if response.status_code == 401:
            session.auth = HTTPDigestAuth(self.username, self.password)
            response = session.get(full_url)
        response.raise_for_status()
        return session

    def session_available(self):
        full_url = urljoin(self.host, '/ISAPI/System/status')
        response = self.session.get(full_url)
        if response.status_code == 200:
            return True
        else:
            return False

    def get_events(self, timeout=30):
        url = urljoin(self.host, "/ISAPI/Event/notification/alertStream")
        try:
            while self.read:
                # print("reading events...")
                response = self.session.request(
                    "get", url, timeout=timeout, stream=True)
                for chunk in response.iter_lines(chunk_size=1024, delimiter=b'--boundary'):
                    if not self.is_open:
                        break
                    if chunk:
                        chunks = chunk.split(b'\r\n\r\n')
                        if len(chunks) < 2:
                            continue
                        try:
                            data = xmltodict.parse(chunks[1].decode("utf-8"))
                            if data['EventNotificationAlert']['eventType'] == "ANPR":
                                self.events.append(data)
                                break
                        except AttributeError:
                            pass
        except ConnectionAbortedError:
            print("ConnectionAbortedError")
        except ConnectionError:
            print("ConnectionError")
        except ReadTimeout:
            print("ReadTimeout")                    
        except (ConnectionError, ReadTimeout, ChunkedEncodingError) as error:
            print(error)
            self.is_open = False
            async_to_sync(self.bg_task.close)()

    def get_pictures(self, width=640, height=360, timeout=3):
        url = urljoin(
            self.host, f"/ISAPI/Streaming/channels/101/picture?videoResolutionWidth={width}&videoResolutionHeight={height}")
        try:
            while self.read:
                # print("reading pictures...")
                start_request = time.time()
                response = self.session.request(
                    "get", url, timeout=timeout, stream=True)
                end_request = time.time()
                self._spend_time_for_picture = end_request - start_request
                if len(self.pictures) >= self.image_queue_size:
                    time.sleep(self.time_interval_pictures)
                    continue
                img_b64 = "data:image/png;base64, " + base64.b64encode(response.content).decode()
                self.pictures.append(img_b64)
                time.sleep(self.time_interval_pictures)
        except (ConnectionError, ReadTimeout, ChunkedEncodingError):
            self.is_open = False
            async_to_sync(self.bg_task.close)()

    def get_spend_time_to_img(self):
        return self._spend_time_for_picture + self.time_interval_pictures
