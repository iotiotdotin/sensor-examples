import smbus

import time

address = 0x48

bus = smbus.SMBus(7)

print('Reading Alcohol values, press Ctrl-C to quit...')

while True:
    bus.write_byte(address,0xA0)
    adc_value = bus.read_byte(address)
    sensor_voltage = (5 * adc_value)/255 
    ppm = (0.025 * sensor_voltage)
    print("Alcohol: %.5f PPM" % ppm)
    time.sleep(0.5)

