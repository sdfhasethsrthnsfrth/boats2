# Expanding a machine vision project
An upgraded system for mapping boat traffic in Valkeakoski
## Description
Thesis project involving Machine Vision with YOLO architecture, LoRaWAN, Raspberry Pi and Node-RED. 


## Getting Started

### Dependencies
* Python library: ultralytics 8.2.18
  ```
  pip install ultralytics==8.2.18
  ```
* Other Python libraries should already be pre-installed: cv2, picamera2, serial, os, time
* OS: Raspberry Pi (x64 Bookworm)


### Hardware
* Raspberry Pi 4B
* Raspberry Pi HQ camera module (C-CS mount)
* C-mount 16mm telephoto lens
* M5Stack 868 LoRaWAN module
* WD Elements 1TB HDD

### Credentials
Are shared through a secure method.

### Preparation
* make sure the serial port of your Pi is enabled:
  ```
  sudo raspi-config
  ```
* in the GUI tool, select `interfaces` and then `serial port`: <br>
  ![raspi-interface](https://github.com/Bonsa-BE/boats/assets/68948638/22c44a3f-e608-4afb-a748-5ccbf180475e)
  
* reboot for the changes to take effect:
  ```
  sudo reboot
  ```
* Download all the code files from the project folder in this repository.
  
* Make all the files in the folder executable and modifiable by all users:
  ```
  sudo chmod +777 /path/to/project/directory/*
  ```
* Make sure your hard drive mounts automatically. A tutorial can be found [here](https://www.digikey.fi/fi/maker/tutorials/2022/how-to-connect-a-drive-hddssd-to-a-raspberry-pi-or-other-linux-computers).
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
  
  This is what it should look like: <br>  ![afbeelding](https://github.com/Bonsa-BE/boats/assets/68948638/d764a18b-9930-44d1-aa18-066055a2ccf0)
* open crontab with the following command:
  ```
  crontab -e
  ```
* to make the heartbeat.py a cronjob, add the following to your crontab:
  ```
  */15 * * * * python3 path/to/heartbeat.py
  ```
* as a final step: make sure the camera is connected to the Pi (__only connect the camera when the Pi is off!__).
* executing following command will try to initialize the camera:
  ```
  libcamera-hello
  ```



### Running program
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
* Whenever you're not sure whether the service is running or not, you can always check its status with following command:
  ```
  sudo systemctl status boats.service
  ```
### System Diagram
![afbeelding](https://github.com/Bonsa-BE/boats/assets/68948638/c026393c-a230-4289-9dff-5b582763607e)

## Authors
Toon Van Havermaet 

Simon Vernaeve

## Version History
* 0.1
    * Initial Release (created by Toon Van Havermaet)
* 0.2
    * Updated model & Hardware (created by Simon Vernaeve)

## License

This project is licensed under the [AGPL-3.0] license - see the LICENSE.md file for details
