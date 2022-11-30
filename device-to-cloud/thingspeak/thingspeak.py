"""
Code puts Fibonnaci numbers to thingspeak
"""

import sys
from time import sleep
import urllib.request


a = 0
b = 1
c = 0
baseURL = 'https://api.thingspeak.com/update?api_key=XRHC5RYTF1308YU7&field1='
while(a < 1000):
	f = urllib.request.urlopen(baseURL +str(a))
	f.read()
	f.close()
	sleep(5)
	c = a
	a = a + b
	b = c 	
print("Program has ended")
