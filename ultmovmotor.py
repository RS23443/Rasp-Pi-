import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the RCWL-1601 pins
OUT_PIN = 23
CK_PIN = 24
GPIO.setup(OUT_PIN, GPIO.IN)
GPIO.setup(CK_PIN, GPIO.IN)

# Set up the motor pins
MOTOR1_PIN = 17
MOTOR2_PIN = 22
GPIO.setup(MOTOR1_PIN, GPIO.OUT)
GPIO.setup(MOTOR2_PIN, GPIO.OUT)

def measure_distance():
    # Measure the pulse width of the OUT signal
    pulse_start = 0
    pulse_end = 0
    while GPIO.input(CK_PIN) == 0:
        pass
    while GPIO.input(CK_PIN) == 1:
        pulse_start = time.time()
        while GPIO.input(OUT_PIN) == 0:
            pass
        pulse_end = time.time()
        break

    # Calculate the distance based on the pulse width
    pulse_width = pulse_end - pulse_start
    distance_cm = 3000 / pulse_width  # rough estimate, adjust as needed

    return distance_cm

def move_motors():
    # Move the motors
    GPIO.output(MOTOR1_PIN, GPIO.HIGH)
    GPIO.output(MOTOR2_PIN, GPIO.HIGH)
    time.sleep(0.5)  # move for 0.5 seconds
    GPIO.output(MOTOR1_PIN, GPIO.LOW)
    GPIO.output(MOTOR2_PIN, GPIO.LOW)

while True:
    # Measure the distance
    distance_cm = measure_distance()

    # If wall is detected, move the motors
    if distance_cm < 20:  # adjust the threshold as needed
        move_motors()
    else:
        # Do nothing if no wall is detected
        pass

    # Wait for 50ms before checking again
    time.sleep(0.05)
