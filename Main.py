# This program will be run to initate total functionality of DORM-E 


import RPi.GPIO as GPIO          
from time import sleep
from pathfind import short_path
from Testing_Sandbox.draft_connect import from_name_to_coordinates
from Testing_Sandbox.draft_connect import from_coordinates_to_distance
import board
import math
import adafruit_lis3mdl



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

#compass setup and offset calibration
i2c = board.I2C()
sensor = adafruit_lis3mdl.LIS3MDL(i2c)
sensor.range = Range.RANGE_4_GAUSS
x_offfset= 12.28
y_offset = 12.77
z_offset = -17.86

def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle

def get_heading(_sensor):
    magnet_x, magnet_y, _ = _sensor.magnetic
    magnet_x += x_offfset
    magnet_y +=y_offset
    return vector_2_degrees(magnet_x, magnet_y)

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

def forward(distance = 1):
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

def rotate(degrees=1):
    adjust_speed(75, 75)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    while ((get_heading(sensor)-degrees) > 1):
        continue
    stop_motors()

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
    print("Shortest Path:" + node_name_list)

    cartesian_coordinate_list = []
    polar_coordinate_list = []

    # array of nodes -> draft connect function
    cartesian_coordinate_list = from_name_to_coordinates(node_name_list)
    polar_coordinate_list = from_coordinates_to_distance(cartesian_coordinate_list)

    for polar_coordinate_pair in polar_coordinate_list:
        # turn first and then distance
        print("orienting to "+ polar_coordinate_pair[1])
        #unblock rotate(polar_coordinate_pair[1])
        # distance
        print("Moving forward "+ polar_coordinate_pair[0] + "meters")
        #unblock forward(polar_coordinate_pair[0])

        # we can't determine if we are at next node because of GPS

    # reversing the list
    print("Arrived at destination. Calculating return route...")
    cartesian_coordinate_list = cartesian_coordinate_list[::-1]
    polar_coordinate_list = from_coordinates_to_distance(cartesian_coordinate_list)

    print("The return route is: "+node_name_list[::-1])
    print("Returning in 10 seconds...")

    # sleep for 10 seconds
    sleep(10)

    for polar_coordinate_pair in polar_coordinate_list:
        # turn first and then distance
        print("orienting to "+ polar_coordinate_pair[1])
        #unblock rotate(polar_coordinate_pair[1])
        # distance
        print("Moving forward "+ polar_coordinate_pair[0] + "meters")
        #unblock forward(polar_coordinate_pair[0])

    print("Delivery Successful!")
    for _ in range(4):
    #unblock rotate(180)
    #unblock rotate(360)
    GPIO.cleanup()

