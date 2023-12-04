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


distanceMultiplier = 84,922.4801


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
sensor = adafruit_lis3mdl.LIS3MDL(i2c)

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

currHeading = 0

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
    adjust_speed(100, 100)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
   

    stop_motors()

def findAngle(target):
    threshold_angle = 3
    consecutive_within_threshold = 0
    threshold_consecutive_readings = 5

    while True:
        mag_x, mag_y, mag_z = sensor.magnetic
        heading = math.atan2(mag_y, mag_x) * (180 / math.pi)

        rotate()

        if abs(heading - target) <= threshold_angle:
            consecutive_within_threshold += 1
            if consecutive_within_threshold >= threshold_consecutive_readings:
                print("Reached the target heading within threshold.")
                stop_motors()
                break  # Exit the loop once the target heading is reached within the threshold for consecutive readings
        else:
            consecutive_within_threshold = 0  # Reset the counter if not consecutive within threshold

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
    start_point = input("Enter the starting point: ")
    end_point = input("Enter the end point: ")
    node_name_list = short_path(start_point, end_point)

    cartesian_coordinate_list = []
    polar_coordinate_list = []

    # array of nodes -> draft connect function
    cartesian_coordinate_list = from_name_to_coordinates(node_name_list)
    
    polar_coordinate_list = from_coordinates_to_distance(cartesian_coordinate_list)
    print(polar_coordinate_list)

    for polar_coordinate_pair in polar_coordinate_list:
        
        convertedDistance = 84922.48010*polar_coordinate_pair[0]
        # turn first and then distance
        print("roating to heading: -2")
        findAngle(-8)
        sleep(3)
        
        # distance
        print("driving (m): "+ str(convertedDistance))
        #forward(polar_coordinate_pair[0])
        forward()
        sleep(convertedDistance)
        stop_motors()
        sleep(3)

        # we can't determine if we are at next node because of GPS

    # reversing the list
    print("reversing path...")
    reversed_cartesian_coordinate_list = cartesian_coordinate_list[::-1]
    reversed_polar_coordinate_list = from_coordinates_to_distance(reversed_cartesian_coordinate_list)
    print("new path:")
    print(polar_coordinate_list)

    # sleep for 10 seconds
    sleep(5)

    for polar_coordinate_pair in reversed_polar_coordinate_list:
        # turn first and then distance
        print("roating to heading: 68")
        findAngle(68)
        sleep(3)
        convertedDistance = 84922.48010*polar_coordinate_pair[0]
       # rotate(polar_coordinate_pair[1])
        
        # distance
        print("driving (m): "+ str(convertedDistance))
       # forward(polar_coordinate_pair[0])
        sleep(convertedDistance)
    GPIO.cleanup()

