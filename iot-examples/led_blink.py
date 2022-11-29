#import the GPIO and time package
import RPi.GPIO as GPIO
import time

LED_PIN = 37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

# loop through 50 times, on/off for 1 second
for i in range(50):
    GPIO.output(LED_PIN,True)
    time.sleep(1)
    GPIO.output(LED_PIN,False)
    time.sleep(1)

GPIO.cleanup()
