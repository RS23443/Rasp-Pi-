import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the RCWL-1601 pin as an input
RCWL_PIN = 17
GPIO.setup(RCWL_PIN, GPIO.IN)

# Define a function to read the distance from the RCWL-1601
def read_distance():
    # Read the signal strength from the RCWL-1601 pin
    signal_strength = GPIO.input(RCWL_PIN)

    # Map the signal strength to a distance estimate ( rough calibration )
    if signal_strength == 1:
        distance_cm = 100  # Very close (less than 10cm)
    elif signal_strength == 0 and GPIO.input(RCWL_PIN) == 1:
        distance_cm = 50  # Close (around 10-20cm)
    elif signal_strength == 0 and GPIO.input(RCWL_PIN) == 0 and GPIO.input(RCWL_PIN) == 1:
        distance_cm = 20  # Medium distance (around 20-40cm)
    else:
        distance_cm = 0  # Far away (more than 40cm)

    return distance_cm

while True:
    # Read the distance from the RCWL-1601
    distance_cm = read_distance()

    # Print the distance to the console
    print(f"Distance to wall: {distance_cm} cm")

    # Wait for 50ms before checking again
    time.sleep(0.05)
