# Sensor Examples 

## What is this?
Simple IoT sensor examples running on BrainyPi. 

## Usage 

1.  Install the dependencies on BrainyPi, run command
    ```sh
    sudo apt-get install python3-dev python3-pip python3-smbus i2c-tools -y
    sudo pip3 install RPi.bme280
    ```
1.  Clone the repository
    ```sh
    git clone https://github.com/iotiotdotin/sensor-examples.git
    ```
1.  Connect the sensors according to the connection diagrams given.
1.  Run the codes
    ```sh
    cd sensor-examples
    sudo python3 ./led_blink.py
    ```
