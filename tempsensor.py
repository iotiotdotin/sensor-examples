import smbus2
import bme280 as sensor
import time

port = 7
address = 0x76
bus = smbus2.SMBus(7)
calibration_params = sensor.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
while True:
    data = sensor.sample(bus, address, calibration_params)

    print("=======================")
    print("Time:", data.timestamp)
    print("Temperature: %f deg C" % data.temperature)
    print("Pressure: %f hPa" % data.pressure)
    time.sleep(1)



