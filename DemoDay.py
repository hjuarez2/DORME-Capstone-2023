# This program will be run to initate total functionality of DORM-E 


import RPi.GPIO as GPIO          
from time import sleep
from pathfind import short_path
from Testing_Sandbox.draft_connect import from_name_to_coordinates
from Testing_Sandbox.draft_connect import from_coordinates_to_distance
import board
from math import atan2, degrees
import adafruit_lis3mdl
import time
from adafruit_lis3mdl import  Range, Rate, PerformanceMode



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
forwardStartHeading = 0

#compass setup and offset calibration
i2c = board.I2C()
sensor = adafruit_lis3mdl.LIS3MDL(i2c)
sensor.Rate = Rate.RATE_155_HZ #ULTRA Acccurate performance
sensor.range = Range.RANGE_4_GAUSS
x_offset= -9.49
y_offset = -10.58
z_offset = 79.62
degree_offset = 0
print("Magnetometer Range: %d Gauss" % Range.string[sensor.range])
print("Magnetometer data_rate is", Rate.string[sensor.data_rate], "HZ")
print("Magnetometer performance_mode is", PerformanceMode.string[sensor.performance_mode])
print("Magnetometer x_offset is ", x_offset)
print("Magnetometer y_offset is ", y_offset)
print("Magnetometer z_offset is ", z_offset)




#distance conversion
timedistance_ratio = 1

def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    angle+=degree_offset
    if angle < 0:
        angle += 360
    return angle

def get_heading(_sensor):
    magnet_x, magnet_y, _ = _sensor.magnetic
    magnet_x += x_offset
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
    adjust_speed(50, 50)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    current_time = time.time()
    target_time = current_time + (distance * timedistance_ratio )
    print(target_time)
    while(current_time < target_time):
        checkHeading(forwardStartHeading)
        current_time = time.time()
    stop_motors()

def checkHeading(target_heading, tolerance = 0.5):
    global lSpeed
    global rSpeed
    global sensor
    current_heading = get_heading(sensor)
    error = (target_heading - current_heading) % 360  # Calculate the error between target and current heading
    print(error)
    if error > 180:
        error -= 360  # Make sure the error is within -180 to 180 degrees range

    #negative error is drifting to right
    #positive error is drifting to left


    if abs(error) > tolerance:
        if error < 0 and rSpeed < 60:
            # Turn left
            print("Adjusting left")
            adjust_steering_angle(-0.1)  # Placeholder function for left adjustment
        elif error > 0 and lSpeed < 60:
            # Turn right
            print("Adjusting right")
            adjust_steering_angle(0.1)  # Placeholder function for right adjustment
            

def adjust_steering_angle(error):
    # Placeholder function to simulate steering adjustment
    adjust_speed(lSpeed+(error),rSpeed+(-error))


def backward(distance=1):
    adjust_speed(50,50)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def rotate(degrees):
    global forwardStartHeading
    forwardStartHeading = degrees
    degrees+=degree_offset
    adjust_speed(40, 40)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    while (abs(get_heading(sensor)-degrees) > 1):
        continue
    print(get_heading(sensor))
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
    for i in range(5):
        rotate(270)
        sleep(1)
        forward(1)
        sleep(1)
        rotate(90)
        sleep(1)
        forward(1)
        sleep(1)
    GPIO.cleanup()

