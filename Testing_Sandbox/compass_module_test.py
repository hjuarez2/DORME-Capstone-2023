#Libraries
import time
import serial
import board
import busio
import adafruit_gps
import adafruit_lis3mdl

# Create a serial connection for the GPS connection using default speed and
# a Raspberry Pi UART /dev/ttyS0
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)

# Create a GPS module instance.
gps = adafruit_gps.GPS(uart, debug=False)

# Turn on the basic GGA and RMC info (what you typically want)
gps.send_command(b'PMTK314,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1')
gps.send_command(b'PMTK220,1000')  # Set update rate to once a second.

# Create I2C device for compass.
i2c = busio.I2C(board.SCL, board.SDA)
compass = adafruit_lis3mdl.LIS3MDL(i2c)

# Main loop runs forever printing the location, etc. every second.
last_print = time.monotonic()
while True:
    # Make sure to call gps.update() every loop iteration and at least twice
    # as fast as data comes from the GPS unit (usually every second).
    gps.update()
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print('Waiting for fix...')
            continue

        # We have a fix! (gps.has_fix is true)
        # Print out details about the fix like location, date, etc.
        print('=' * 40)  # Print a separator line.
        print(f'Fix timestamp: {gps.timestamp_utc.tm_year}/{gps.timestamp_utc.tm_mon}/{gps.timestamp_utc.tm_mday} {gps.timestamp_utc.tm_hour}:{gps.timestamp_utc.tm_min}:{gps.timestamp_utc.tm_sec}')
        print(f'Latitude: {gps.latitude:.6f} degrees')
        print(f'Longitude: {gps.longitude:.6f} degrees')
        print(f'Fix quality: {gps.fix_quality}')

        # Now read the compass data
        mag_x, mag_y, mag_z = compass.magnetic

        print(f'Magnetometer X: {mag_x:<5.2f} Y: {mag_y:<5.2f} Z: {mag_z:<5.2f} uT')
        # Calculate the heading
        heading = (math.atan2(mag_y, mag_x) * 180) / math.pi
        # Normalize to 0-360
        if heading < 0:
            heading += 360
        print(f'Heading: {heading:.2f} degrees')
