import RPi.GPIO as GPIO          
from time import sleep
import sys

# Initialization
in1 = 24
in2 = 23
in3 = 17
in4 = 27
speedrate = 0.30842857142857
turnrate = 10
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
    adjust_speed('low')
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    time.sleep(speedrate*distance)
    stop_motors()

def backward(distance=1):
    adjust_speed('low')
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    time.sleep(speedrate*distance)
    stop_motors()

def rotate(degrees=1):
    adjust_speed('low')
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    time.sleep(turnrate*degrees)
    stop_motors()

def adjust_speed(level):
    if level == 'low':
        p1.ChangeDutyCycle(30)
        p2.ChangeDutyCycle(30)
        speedrate = 0.30842857142857
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

    sleep(15)
    p1.ChangeDutyCycle(30)
    p2.ChangeDutyCycle(30)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    sleep(2)
    GPIO.cleanup()

    
    while False:
        x = input()
        if x == 'r':
            forward()
            print("run forward")
        elif x == 's':
            stop_motors()
            print("stop")
        elif x == 'f':
            forward()
            print("forward")
        elif x == 'b':
            backward()
            print("backward")
        elif x == 'l':
            adjust_speed('low')
            print("low")
        elif x == 'm':
            adjust_speed('medium')
            print("medium")
        elif x == 'h':
            adjust_speed('high')
            print("high")
        elif x == 'e':
            GPIO.cleanup()
            print("GPIO Clean up")
            break
        else:
            print("<<<  wrong data  >>>")
