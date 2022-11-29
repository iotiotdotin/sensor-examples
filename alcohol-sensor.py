import smbus
import time

I2C_PORT = 7
PCF8591_ADDR = 0x48
bus = smbus.SMBus(I2C_PORT)

while True:
    bus.write_byte(PCF8591_ADDR, A0)
    value = bus.read_byte(PCF8591_ADDR)
    print("=======================")
    print("Alcohol range: %f PPM" % value)
    time.sleep(1)
