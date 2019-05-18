#######################################################
#Engineering World Health Optical Heart Rate Monitor
#RParkerE
#Python code for BBB heart monitor display
#heart_rate_monitor_BBB.py
#######################################################

#! /usr/bin/python

import Adafruit_BBIO.ADC as ADC
import time

heart_rate_pin = "P9_34"        #GPIO Pin Number 


HIGH = 0.4	# Value that represents a "heartbeat" 
Low = 0.3	# Value that represents lack of "heartbeat"

# Code to display information to LCD

def display (value):

# Code to calculate beats per minute

    def main():
        ADC.setup()
        beats = []
        Low_to_High = False
        High_to_Low = False

while True:
	reading = ADC.read(heart_rate_pin)
	if (reading > HIGH) and (Low_to_High == False):
		beats.append(time.time())
		Low_to_High = True
		High_to_Low = False
		sleep.time(0.00667)
	elif (reading < LOW) and (High_to_Low == False):
		High_to_Low == True
		Low_to_High == False
		sleep.time(0.00667)
	if (len(beats) >= 60):
		bpm = (len(beats)/((beats[len(beats)]-beats[0])/60.0))
		beats.pop(0)
		display (bpm)
