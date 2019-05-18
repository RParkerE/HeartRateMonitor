#######################################################
#Engineering World Health Optical Heart Rate Monitor
#RParkerE
#Python code for RPi heart monitor display
#heart_rate_monitor.py
#######################################################

#! /usr/bin/python
 
import RPi.GPIO as GPIO
import time
 
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

import Image
import ImageDraw
import ImageFont

# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Raspberry Pi software SPI config:
# SCLK = 4
# DIN = 17
# DC = 23
# RST = 24
# CS = 8

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
#disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white filled box to clear the image.
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
	
def display(value):  # Code to display information to LCD
    # Load default font.
    font = ImageFont.load_default()

    # Alternatively load a TTF font.
    # Some nice fonts to try: http://www.dafont.com/bitmap.php
    # font = ImageFont.truetype('Minecraftia.ttf', 8)

    # Write some text.
    draw.text((8, 10), 'Heart Rate:', font=font)
    draw.text((17, 23), value, font=font)
    draw.text((40, 23), 'BPM', font=font)

    # Display image.
    disp.image(image)
    disp.display()
 
heart_rate_pin = 17  # GPIO Pin Number
GPIO.setmode(GPIO.BCM) # Sets GPIO mode as GPIO pins
GPIO.setup(heart_rate_pin, GPIO.IN) # Makes heart_rate_pin read as input
 
beats = []
Low_to_High = False
High_to_Low = False
start_time = time.time()
while True:
	# Reads GPIO input
    reading = GPIO.input(heart_rate_pin)
	# Sees if there is a beat and counts it
    if reading == True and Low_to_High == False:
	    beats.append(time.time())
	    Low_to_High = True
	    High_to_Low = False
	# Sees if there is no beat and resets
    elif reading == False and High_to_Low == False:
	    High_to_Low = True
	    Low_to_High = False
	# Calculates and displays the beats per minute from GPIO input
    if (len(beats) >= 30):
	    bpm = (int(len(beats)/((beats[len(beats)-1]-beats[0])/60.0)))
	    bpm = str(bpm)
	    display(bpm)
		# Reset the list beats
	    del beats[:]
