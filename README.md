# Status App

This is application that will show You some information about Your CPU and memory.

## Brief description

   NOTE: please use following command before starting:
````bash
sudo socat -d -d pty,raw,echo=0,link=/dev/ttyS20 pty,raw,echo=0,link=/dev/ttyS21
````
This will create bidarectional streams link to /dev/ttyS20 and S21, which are used in app.

### Daemon.py

Daemon class is responsoble for getting information about CPU and memory.
Then with help of Protobuf it sends collected data through serial port to the listener.


### Listener.py

Listener class is responsible for receiving the data and then store it in json file.


### What's next?

Collected data will be visualized in web page in real time manner.
