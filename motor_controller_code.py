import RPi.GPIO as GPIO
import time

# Configure the GPIO settings
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins connected to the L298N
IN1 = 23  # Connect to IN1 on the L298N
IN2 = 24  # Connect to IN2 on the L298N
ENA = 18  # Connect to ENA on the L298N

# Setup the GPIO pins
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# Setup PWM for ENA
pwm = GPIO.PWM(ENA, 100)
pwm.start(0)  # Start with duty cycle 0%

# Function to move the motor forward
def forward(speed):
    pwm.ChangeDutyCycle(speed)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)

# Function to move the motor backward
def backward(speed):
    pwm.ChangeDutyCycle(speed)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)

# Function to stop the motor
def stop():
    pwm.ChangeDutyCycle(0)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)

# Main loop
try:
    while True:
        print("Moving forward")
        forward(50)  # Move forward at 50% speed
        time.sleep(2)  # Run for 2 seconds
        
        print("Stopping")
        stop()  # Stop
        time.sleep(1)  # Wait for 1 second

        print("Moving backward")
        backward(50)  # Move backward at 50% speed
        time.sleep(2)  # Run for 2 seconds
        
        print("Stopping")
        stop()  # Stop
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    print("Ctrl+C pressed. Stopping motor.")
    stop()
    GPIO.cleanup()

        
