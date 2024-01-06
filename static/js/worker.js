let session = null,
  ports = [];


self.addEventListener(
  "connect",
  function (e) {
    let port = e.ports[0];
    port.start();

    port.addEventListener(
      "message",
      function (e) {
        if (e.data.connect) {
          if (session === null) {
            const xhr = new XMLHttpRequest();
            xhr.addEventListener("readystatechange", function () {
              if (this.readyState == 4 && this.status == 200) {
                const wsport = this.responseText;
                if (wsport == 0) {
                  port.postMessage({ open: false });
                  return;
                }
                
                session = new WebSocket(`ws://${e.data.hostname}:${wsport}/`);
                session.addEventListener("message", function (msg) {
                  session.send(0);
                });
                
                session.addEventListener("message", function (msg) {
                  port.postMessage({ open: true, data: msg.data });
                });
              }
            });
            
            xhr.open(
              "GET",
              `${e.data.protocol}//${e.data.hostname}:${e.data.port}/devices/scales/connect/${e.data.scaleId}`
              );
              xhr.send();
          } else {
            session.addEventListener("message", function (msg) {
              port.postMessage({ open: true, data: msg.data });
            });
          }

        } else {
          session.close();
          port.postMessage({ open: false, closed: true});
        }
      },
      false
    );
  },
  false
);
