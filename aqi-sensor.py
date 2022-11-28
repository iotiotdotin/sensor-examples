import smbus
import time
address = 0x48
bus = smbus.SMBus(7)

while True:
    bus.write_byte(address,A0)
    value = bus.read_byte(address)
    print(value)
    time.sleep(0.1)
