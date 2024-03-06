const ws_connections = {};

function start_ipcamera_ws_connection(element) {
  const id = element.dataset.id;
  const name_ws = element.dataset.name;
  if (id === undefined || name_ws === undefined) {
    console.error("'name' or 'id' is not provided");
    return;
  }

  const img = element.querySelector(".js-display");
  if (img === null) {
    console.error("class 'js-display' not found");
    return;
  }

  let inpPhoto;
  if (img.dataset.save) {
    inpPhoto = document.querySelector(`input[name=${img.dataset.name}]`);
    if (inpPhoto === null) {
      console.error("img and input tags' names are not matching");
      return;
    }

    function readerOnLoad(inp, reader) {
      inp.value = reader.result;
    }
  }

  img.onload = function () {
    URL.revokeObjectURL(this.src); // release the blob URL once the image is loaded
  };

  const ws = new WebSocket(`ws://localhost:8000/ws/ipcamera/${id}/`);
  ws_connections[name_ws] = ws;

  ws.addEventListener("message", function (event) {
    const data = JSON.parse(event.data);
    if (data["ok"] && data["image_b64"]) {
      // img.src = URL.createObjectURL(event.data);
      img.src = data["image_b64"];
      if (inpPhoto) {
        const reader = new FileReader();
        reader.onload = (e) => readerOnLoad(inpPhoto, reader);
        reader.readAsDataURL(event.data);
      }
    } else {
      if (data["ok"]) {
        const anpr = data["data"]["EventNotificationAlert"]["ANPR"];
        const licensePlate = anpr["licensePlate"];

        console.log(`Detected license plate '${licensePlate}'`);
        const plateIndicator = document.querySelector(".js-license_plate");
        if (plateIndicator) plateIndicator.textContent = licensePlate;

        const inpPlate = document.querySelector(".js-plate");
        if (inpPlate) {
          inpPlate.value = licensePlate;
        }

        const inpVehicle = document.querySelector(".js-vehicle");
        if (inpVehicle) {
          fetch(
            `${location.origin}/api/catalogs/vehicles/detail/${licensePlate}/`
          )
            .then((res) => {
              if (res.status == 200) {
                return res.json();
              } else if (res.status == 404) {
                inpVehicle.value = 0;
                console.log(
                  `Vehicle not found with this registration plate '${licensePlate}'`
                );
                throw new Error(res.statusText);
              } else {
                throw new Error(res.statusText);
              }
            })
            .then((data) => {
              inpVehicle.value = data.id;
            })
            .catch((err) => console.error(`Something went wrong. ${err}`));
        }
      } else {
        img.src = "";
        const plateIndicator = document.querySelector(".js-license_plate");
        if (plateIndicator) plateIndicator.textContent = "";
        
        console.log(data["message"]);
      }
    }
  });

  ws.addEventListener("close", function (event) {
    const plateIndicator = document.querySelector(".js-license_plate");
    if (plateIndicator) plateIndicator.textContent = "";
    
    if (ws_connections[name_ws]) {
      ws_connections[name_ws] = undefined;
    }
  });

  ws.addEventListener("error", function (event) {
    alert("Connection problem!");
  });
}

function start_truckscale_ws_connection(element) {
  const id = element.dataset.id;
  const name_ws = element.dataset.name;
  if (id === undefined || name_ws === undefined) {
    console.error("'name' or 'id' is not provided");
    return;
  }

  const indicator = element.querySelector(".js-display");
  if (indicator === null) {
    console.error("class 'js-display' not found");
    return;
  }
  const ws = new WebSocket(`ws://localhost:8000/ws/truckscale/${id}/`);
  ws_connections[name_ws] = ws;

  ws.addEventListener("message", function (event) {
    const data = JSON.parse(event.data);
    if (data["ok"]) {
      indicator.textContent = data["data"];
    } else {
      indicator.textContent = "-";
      console.log(data["message"]);
    }
  });

  ws.addEventListener("close", function (event) {
    if (ws_connections[name_ws]) {
      ws_connections[name_ws] = undefined;
    }
  });

  ws.addEventListener("error", function (event) {
    alert("Connection problem!");
  });
}

function send_message(element, method) {
  const name_ws = element.dataset.name;
  if (name_ws === undefined) {
    console.error("'name' is not provided");
    return;
  }
  let ws = ws_connections[name_ws];

  if (!ws) {
    if (element.classList.contains("js-truckscale")) {
      start_truckscale_ws_connection(element);
    } else if (element.classList.contains("js-ipcamera")) {
      start_ipcamera_ws_connection(element);
    }
    ws = ws_connections[name_ws];
  }

  if (ws) {
    let message;
    if (method === "POST") {
      console.log("post");
      if (element.querySelector(".js-device") === null) {
        console.error("class 'js-device' is not found");
        return;
      }

      const pk = element.querySelector(".js-device").value;
      element.dataset["pk"] = pk;
      message = {
        method: method,
        pk: pk,
      };
    } else if (method === "DELETE") {
      message = {
        method: method,
      };
    }

    if (message) {
      if (ws.readyState === ws.OPEN) {
        ws.send(JSON.stringify(message));
      } else if (ws.readyState === ws.CONNECTING) {
        _send = () => {
          if (ws.readyState === ws.OPEN) {
            ws.send(JSON.stringify(message));
          } else if (ws.readyState === ws.CONNECTING) {
            setTimeout(_send, 1000);
          }
        };
        setTimeout(_send, 1000);
      }
    }
  } else {
    console.error("There is no websocket connection");
  }
}

function start(element) {
  send_message(element, "POST");
}

function stop(element) {
  send_message(element, "DELETE");
}

document.querySelectorAll(".js-ipcamera").forEach(function (el) {
  el.addEventListener("click", function (event) {
    if (event.target.classList.contains("js-camera-on")) {
      start(el);
    } else if (event.target.classList.contains("js-camera-off")) {
      stop(el);
    }
  });
});

document.querySelectorAll(".js-ipcamera").forEach(function (el) {
  start_ipcamera_ws_connection(el);
});

document.querySelectorAll(".js-truckscale").forEach(function (el) {
  el.addEventListener("click", function (event) {
    if (event.target.classList.contains("js-scale-on")) {
      start(el);
    } else if (event.target.classList.contains("js-scale-off")) {
      stop(el);
    }
  });
});

document.querySelectorAll(".js-truckscale").forEach(function (el) {
  start_truckscale_ws_connection(el);
});
