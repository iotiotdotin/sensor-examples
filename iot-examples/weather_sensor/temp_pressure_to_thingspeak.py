import smbus2
import bme280 as sensor
import time
import urllib.request

def send_to_thingspeak(field, value):
    baseURL = 'https://api.thingspeak.com/update?api_key=XRHC5RYTF1308YU7&field'+ str(field) + '='
    f = urllib.request.urlopen(baseURL + str(value))
    f.read()
    f.close()


I2C_PORT = 7
BME280_ADDR = 0x76

bus = smbus2.SMBus(I2C_PORT)
calibration_params = sensor.load_calibration_params(bus, BME280_ADDR)

# the sample method will take a single reading and return a
# compensated_reading object
while True:
    data = sensor.sample(bus, BME280_ADDR, calibration_params)

    print("=======================")
    print("Time:", data.timestamp)
    print("Temperature: %f deg C" % data.temperature)
    print("Pressure: %f hPa" % data.pressure)
    send_to_thingspeak(1, data.temperature)
    send_to_thingspeak(2, data.pressure)

    time.sleep(1)



