import RPi.GPIO as GPIO
from time import sleep

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Motor Pins: replace with the GPIO pins you're using
Motor1A = 18
Motor1B = 23
Motor1E = 24

# Setup GPIO pins
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

print("Turning motor on")

# Forward rotation
GPIO.output(Motor1A, GPIO.HIGH)  # Set Motor1A pin to HIGH
GPIO.output(Motor1B, GPIO.LOW)   # Set Motor1B pin to LOW
GPIO.output(Motor1E, GPIO.HIGH)  # Enable the motor

# Wait for 2 seconds
sleep(2)

# Stop the motor
print("Stopping motor")
GPIO.output(Motor1E, GPIO.LOW)  # Disable the motor

# Cleanup GPIO
GPIO.cleanup()
