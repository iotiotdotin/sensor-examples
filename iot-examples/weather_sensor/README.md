## Description

Read temperature and pressure values from BME280/BMP280 sensor.


## Usage 

1.  Install dependencies on BrainyPi
    ```sh
    sudo apt-get install python3-dev python3-pip python3-smbus i2c-tools -y
    sudo pip3 install RPi.bme280
    ```

1.  Clone the repository
    ```sh
    git clone https://github.com/iotiotdotin/sensor-examples.git
    cd sensor-examples/iot-examples/weather_sensor
    ```
   
1.  Connect the sensors according to the connection diagrams given.
    ![Diagram](./connection_diagram.png)
    
1.  Create Thingspeak account (Skip if you already have one)
    1.  Go to the site - https://thingspeak.com/
    1.  Click on "Get started for free"
        ![ss1](/device-to-cloud/thingspeak/screenshots/Screenshot_20221129_215419.png)
    1.  Verify your email ID
        ![ss1](/device-to-cloud/thingspeak/screenshots/Screenshot_20221129_215535.png)
    1.  Account should be created.

1.  Create Thingspeak Channel 
    1.  Click on "New Channel"
        ![ss1](/device-to-cloud/thingspeak/screenshots/Screenshot_20221129_215641.png)
    1.  Fill in the Name and Description.
    1.  Check all fields and name them
        ![ss1](/device-to-cloud/thingspeak/screenshots/Screenshot_20221130_065702.png)
    1.  Save your channel. 
    
1.  Copy the channel link 
    ![ss1](/device-to-cloud/thingspeak/screenshots/Screenshot_20221129_215729.png)

1.  Paste the channel link in the code 
  
    ![ss1](/device-to-cloud/thingspeak/screenshots/Screenshot_20221130_071043.png)
    
1.  Delete the `1=0` at the end of the channel code link, for eg:
    
    -   Copied channel code `https://api.thingspeak.com/update?api_key=XRHC5RYTF1308YU7&field1=0`
    -   Modified channel code `https://api.thingspeak.com/update?api_key=XRHC5RYTF1308YU7&field`  

    
1.  Run the code
    ```sh
    sudo python3 ./weather_sensor.py
    ```
