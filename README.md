# dht22-on-raspberrypi

Using dht22 sensor to collect temperature and humidity data onto raspberry pi
Currently, there is no latest update on using python to get dht22 sensor data
on raspberry pi. 

This is an update focusing on what to install and how to install 

## Getting started

### Environment

1. For the system environment, use raspberry pi imager to install raspbien into
the SD card. 

2. After setting up your raspberry pi, update and upgrade apt, according to 
official statement, you should alway use full-upgrade when upgrading.

```Bash

sudo apt update && sudo apt full-upgrade
```

3. Create a virtural environment. raspbien has enviromental package control,
trying to instll package directly will result in error.

    1. create a directory that store the project
        
```Bash

mkdir <folder-name> 
```

    2. Head into the folder, create a virtural environment with venv

```Bash
cd <folder-name>; python -m venv <env-name>
```

    3. Activate the virtual environment.

```Bash
source <env-name>/bin/activate
```

* Now for Updated part. Using python to control dht22, you need python
package 'adafruit-dht' in order to use the sensor. However the original 
package is archived, so most of the example that uses this package can not 
installed. Currently the only one that supports python is 
adafruit-circuitpython-dht, which is included in the requirement.txt

```Bash
pip install -r requirement.txt
```

#### dht22 Setup

set the dht with + to 5v, - to ground, and out to one of the GPIO pin
(GPIO 4 were use in these repository).

### Deployment

#### Get Repository

1. Clone this repository into the folder.

```bash
git clone https://github.com/ya01in/dht22-on-raspberrypi.git
```

2. run the testing demo code

```bash
python3 /dht22-on-raspberrypi/sensor/demo.py
```

