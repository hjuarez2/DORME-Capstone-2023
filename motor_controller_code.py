# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

# Libraries
import RPi.GPIO as GPIO          
from time import sleep

# Pin configuration
in1 = 24
in2 = 23
in3 = 17
in4 = 27
ena = 12
enb= 13
temp1=1

# GPIO setup
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
p1=GPIO.PWM(ena,1000)
p2=GPIO.PWM(enb,1000)

p1.start(25)
p2.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")


while(1):

    x=input()
    
    # Run
    if x=='r':
        print("run")

        # Forward
        if(temp1==1):
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            print("forward")
            x='z'

        # Backwards
        else:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            print("backward")
            x='z'

    # Stop
    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    # Forward
    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'

    # Backward
    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=0
        x='z'

    # Low speed
    elif x=='l':
        print("low")
        p1.ChangeDutyCycle(10)
        p2.ChangeDutyCycle(10)
        x='z'

    # Medium speed
    elif x=='m':
        print("medium")
        p1.ChangeDutyCycle(20)
        p2.ChangeDutyCycle(20)
        x='z'

    # High speed
    elif x=='h':
        print("high")
        p1.ChangeDutyCycle(35)
        p2.ChangeDutyCycle(35)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enater the defined data to continue.....")

# functions to create
# forward(distance (in meters))
# backwards(distance (in meters))
# rotate(degrees)
# adjust_speed(level (which is either low medium or high))