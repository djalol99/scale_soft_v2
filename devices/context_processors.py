import pickle
import os
os.path.dirname((os.path.abspath(__file__)))

PATH = os.path.join(os.path.dirname(
    (os.path.abspath(__file__))), "data", "devices.pkl")


def devices(request):
    check_file()
    with open(PATH, 'rb') as f:
        data = pickle.load(f)
        print(data)
    return data


def check_file():
    if not os.path.isfile(PATH) or os.path.getsize(PATH) == 0:
        with open(PATH, 'wb') as f:
            data = {
                "truckscale_1": 0,
                "ipcamera_1": 0,
                "ipcamera_2": 0
            }
            pickle.dump(data, f)


def update_data(key, value):
    check_file()
    with open(PATH, 'rb+') as f:
        data = pickle.load(f)
        data[key] = value
        f.seek(0)
        f.truncate()
        pickle.dump(data, f)
