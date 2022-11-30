## Description

Send data (fibonnaci numbers) to Thingspeak cloud.


## Usage 

1.  Clone the repository
    ```sh
    git clone https://github.com/iotiotdotin/sensor-examples.git
    cd sensor-examples/device-to-cloud/thingspeak
    ```
1.  Create Thingspeak account
    1.  Go to the site - https://thingspeak.com/
    1.  Click on "Get started for free"
        ![ss1](./screenshots/Screenshot_20221129_215419.png)
    1.  Verify your email ID
        ![ss1](./screenshots/Screenshot_20221129_215535.png)
    1.  Account should be created.

1.  Create Thingspeak Channel
    1.  Click on "New Channel"
        ![ss1](./screenshots/Screenshot_20221129_215641.png)
    1.  Fill in the Name and Description.
    1.  Check all fields and name them
        ![ss1](./screenshots/Screenshot_20221130_065702.png)
    1.  Save your channel. 
    
1.  Copy the channel link 
    ![ss1](./screenshots/Screenshot_20221129_215729.png)

1.  Paste the channel link in the code 
  
    ![ss1](./screenshots/Screenshot_20221130_070012.png)
    
1.  Delete the `0` at the end of the channel code link, for eg:
    
    -   Copied channel code `https://api.thingspeak.com/update?api_key=XRHC5RYTF1308YU7&field1=0`
    -   Modified channel code `https://api.thingspeak.com/update?api_key=XRHC5RYTF1308YU7&field1=`
    

1.  Run the code
    ```sh
    sudo python3 ./thingspeak.py
    ```
    
1.  The data should be displayed on Thingspeak.

    ![ss1](./screenshots/Screenshot_20221129_220140.png)

    
