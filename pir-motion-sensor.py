import RPi.GPIO as GPIO
import time

SENSOR_PIN = 40
LED_PIN = 37

GPIO.setmode(GPIO.BOARD)
#Read output from PIR motion sensor
GPIO.setup(SENSOR_PIN, GPIO.IN)   
#LED output pin      
GPIO.setup(LED_PIN, GPIO.OUT)  

while True:
    sensor_value = GPIO.input(SENSOR_PIN)
    if sensor_value == GPIO.LOW: #When output from motion sensor is LOW
        print("No Motion detected.")
        GPIO.output(LED_PIN, GPIO.LOW) #Turn OFF LED
        time.sleep(0.1)
    elif sensor_value == GPIO.HIGH: #When output from motion sensor is HIGH
        print("Motion detected.")
        GPIO.output(LED_PIN, GPIO.HIGH)  #Turn ON LED
        time.sleep(0.1)
