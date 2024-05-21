# Machine Vision in a Marine Environment
Mapping boat traffic in Valkeakoski
## Description
Thesis project involving Machine Vision with YOLO architecture, LoRaWAN, Raspberry Pi and Node-RED. 


## Getting Started

### Dependencies
* This project relies on Python libraries: YOLO, opencv
* Other Python libraries should already be installed: picamera2, serial, os, time
* OS: Raspberry Pi (x64 Bookworm)





### Installing

* Download all the code.
* Make all the files in the folder executable and modifiable by all users:
  ```
  sudo chmod +777 /path/to/project/directory/*
  ```
* Make sure your hardrive mounts automatically. A tutorial can be found [here](https://www.digikey.fi/fi/maker/tutorials/2022/how-to-connect-a-drive-hddssd-to-a-raspberry-pi-or-other-linux-computers).
* create a systemd service for the main.py file.
```
sudo nano etc/systemd/system/name_of_service.service
```
  This is what it should look like: <br> ![afbeelding](https://github.com/Bonsa-BE/boats/assets/68948638/d764a18b-9930-44d1-aa18-066055a2ccf0)
* to make the heartbeat.py a cronjob, add the following to your crontab:
```
crontab -e
```

```
*/15 * * * * python3 path/to/heartbeat.py
```



### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors
Toon Van Havermaet  

## Version History
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
