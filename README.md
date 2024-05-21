# Machine Vision in a Marine Environment
Mapping boat traffic in Valkeakoski
## Description
Thesis project involving Machine Vision with YOLO architecture, LoRaWAN, Raspberry Pi and Node-RED. 


## Getting Started

### Dependencies
* This project relies on Python libraries: YOLO, opencv
* Other Python libraries should already be installed: picamera2, serial, os, time
* OS: Raspberry Pi (x64 Bookworm)





### Installing and running code

* Download all the code.
* Make all the files in the folder executable and modifiable by all users:
  ```
  sudo chmod +777 /path/to/project/directory/*
  ```
* Make sure your hardrive mounts automatically. A tutorial can be found [here](https://www.digikey.fi/fi/maker/tutorials/2022/how-to-connect-a-drive-hddssd-to-a-raspberry-pi-or-other-linux-computers).
* create a systemd service for the main.py file (in this case it is called boats.service):
```
sudo nano etc/systemd/system/boats.service
```
```
[Unit]
Description=start monitoring boats
Afer=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/Captain/project/main.py
Restart=on-failure
RestartSec=60s
StartLimitInterval=180s
StartLimitBurst=3

[Install]
WantedBy=multi-user.target
```
  This is what it should look like: <br> ![afbeelding](https://github.com/Bonsa-BE/boats/assets/68948638/d764a18b-9930-44d1-aa18-066055a2ccf0)
* open crontab with the following command:
```
crontab -e
```
* to make the heartbeat.py a cronjob, add the following to your crontab:


```
*/15 * * * * python3 path/to/heartbeat.py
```
* as a final step: make sure the camera is connected to the Pi (only connect the camera when the Pi is off!).
* executing following command will try to initialize the camera:
```
libcamera-hello
```



### Executing program

* The program will run automatically on boot. You can check the status of the systemd service with following command:
```
sudo systemctl satus boats.service
```

## What about maintenance?

* As a best practice, first stop the systemd service from running. This will properly close the code:
```
sudo systemctl stop boats.service
```
* Next, reload the systemd daemon, to make sure the stop went through:
```
sudo systemctl daemon-reload
```
* Now you can do any maintenance you like
* After maintenance, don't forget to restart the service again:
  ```
  sudo systemctl start boats.service
  ```
* And to make sure the start went through, reload the systemd daemon again:
  ```
  sudo systemctl daemon-reload
  ```

## Authors
Toon Van Havermaet  

## Version History
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details
