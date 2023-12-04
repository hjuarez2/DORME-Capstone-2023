import board
import busio
import adafruit_lis3mdl
import math

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create sensor object
sensor = adafruit_lis3mdl.LIS3MDL(i2c)

# Optionally adjust sensor settings
sensor.range = adafruit_lis3mdl.RANGE_4_GAUSS  # Set the range to 4 Gauss

# Function to calculate heading
def calculate_heading():
    mag_x, mag_y, _ = sensor.magnetic  # Read magnetic data

    # Calculate heading
    heading = math.atan2(mag_y, mag_x) * 180 / math.pi
    if heading < 0:
        heading += 360

    return heading

while True:
    heading = calculate_heading()
    print("Heading: {:.2f} degrees".format(heading))
