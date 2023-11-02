# This program will be run to initate total functionality of DORM-E 

#import Course_Correction.py as cc
#import Path_Selection.py as ps
#import sensors as ss
#import draft_pathfind.py as pf
package import RPi.GPIO as GPIO          
from time import sleep
#import motor_controller_code_function.py as mc

# Initialization
in1 = 24
in2 = 23
in3 = 17
in4 = 27
ena = 12
enb = 13

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

def forward(distance=1):
    adjust_speed(low)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    time.sleep(1*distance)
    stop_motors()

def backward(distance=1):
    adjust_speed(low)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    time.sleep(1*distance)
    stop_motors()

def rotate(degrees=1):
    adjust_speed(high)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    time.sleep(1*degrees)
    stop_motors()

def adjust_speed(level):
    if level == 'low':
        p1.ChangeDutyCycle(10)
        p2.ChangeDutyCycle(10)
    elif level == 'medium':
        p1.ChangeDutyCycle(20)
        p2.ChangeDutyCycle(20)
    elif level == 'high':
        p1.ChangeDutyCycle(35)
        p2.ChangeDutyCycle(35)
    else:
        print("Invalid speed level")

def stop_motors():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

if __name__ == "__main__":

    mc.forward()

    
    #n = len(sys.argv)
    
    #path = a_star(sys.argv[1], sys.argv[2], sys.argv[3])
    #currentNode=sys.argv[1]

    #for i in range(0,len(path)):
        #driveto(currentNode,path[i])


