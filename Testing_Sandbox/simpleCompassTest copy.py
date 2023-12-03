# This program will be run to initate total functionality of DORM-E 

#import Course_Correction.py as cc
#import Path_Selection.py as ps
#import sensors as ss
#import draft_pathfind.py as pf
import RPi.GPIO as GPIO          
from time import sleep
from pathfind import short_path
from Testing_Sandbox.draft_connect import from_name_to_coordinates
from Testing_Sandbox.draft_connect import from_coordinates_to_distance
import board
import math
import adafruit_lis3mdl

i2c = board.I2C() # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C() # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_lis3mdl.LIS3MDL(i2c)


#import motor_controller_code_function.py as mc

# Pin setup and Constants
in1 = 24
in2 = 23
in3 = 17
in4 = 27
ena = 12
enb = 13

lSpeed = 75
rSpeed = 75

#Distance and Angle Conversion
meter=3
degree=1

#compass setup
i2c = board.I2C()


#GPIO initialization
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p1 = GPIO.PWM(ena,1000)
p2 = GPIO.PWM(enb,1000)
p1.start(25)
p2.start(25)

def forward():
    adjust_speed(75, 75)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)


def backward(distance=1):
    adjust_speed(50,50)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def rotate():
    adjust_speed(25, 25)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def adjust_speed(left, right):
    global lSpeed
    global rSpeed 
    lSpeed = left
    rSpeed = right
    p1.ChangeDutyCycle(lSpeed)
    p2.ChangeDutyCycle(rSpeed)


def stop_motors():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

if __name__ == "__main__":
   while True:
      mag_x, mag_y, mag_z = sensor.magnetic
      heading = math.atan2(mag_y, mag_x) * (180 / math.pi)
      if heading < 0:
         heading += 360

      rotate()
      if(heading>90):
          stop_motors()
          time.sleep(5)

      
