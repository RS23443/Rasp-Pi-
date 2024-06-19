import gpiozero
from time import sleep, time
import RPi.GPIO as GPI1 # for color sensor program


# GPIO values for the signal and photoreceptor pins - color sensor - new gpio number since they interfere with the motor numbers
s2 = 23
s3 = 24
signal = 25
NUM_CYCLES = 10

button_on = gpiozero.Button(2)
button_off = gpiozero.Button(3)
#number is where the button is on the pins on the RPI board

fl = gpiozero.Motor(4,14)
fr = gpiozero.Motor(17,18)
ml = gpiozero.Motor(6,12)
mr = gpiozero.Motor(26,20)
br = gpiozero.Motor(22,23)
bl = gpiozero.Motor(9,25)  
# labeling the motors

drivetrain = gpiozero.Robot(left = lm and bl and fl, right= fr and mr and br)
# this declares the robo and its motor

# on function - just test code inside for now
def on(): 
  if button_on is pressed:
    drivetrain.forward()
    sleep(5)
    drivetrain.right()
    sleep(5)
    drivetrain.left()
    sleep(5)
    drivetrain.backward()
    sleep(5)
    
# off function, turns robo off
def off():
  if button_off is pressed:
    drivetrain.stop()

# def endprogram():
    # GPI1.cleanup()
# end program function

# defs the setup for the color sensor program
def setup():
  GPI1.setmode(GPI1.BCM)
  GPI1.setup(signal,GPI1.IN, pull_up_down=GPI1.PUD_UP)
  GPI1.setup(s2,GPI1.OUT)
  GPI1.setup(s3,GPI1.OUT)
  print("\n")

# defining the rgb values and what each value represents
def loop():
  temp = 1
  while(1):  

    GPI1.output(s2,GPI1.LOW)
    GPI1.output(s3,GPI1.LOW)
    sleep(0.3)
    start = time()
    for impulse_count in range(NUM_CYCLES):
      GPI1.wait_for_edge(signal, GPI1.FALLING)
    duration = time() - start 
    red  = NUM_CYCLES / duration   
   
    GPI1.output(s2,GPI1.LOW)
    GPI1.output(s3,GPI1.HIGH)
    sleep(0.3)
    start = time()
    for impulse_count in range(NUM_CYCLES):
      GPI1.wait_for_edge(signal, GPI1.FALLING)
    duration = time() - start
    blue = NUM_CYCLES / duration
    

    GPI1.output(s2,GPI1.HIGH)
    GPI1.output(s3,GPI1.HIGH)
    sleep(0.3)
    start = time()
    for impulse_count in range(NUM_CYCLES):
      GPI1.wait_for_edge(signal, GPI1.FALLING)
    duration = time() - start
    green = NUM_CYCLES / duration
    
# values are <7000 and >12000 -> for the RGB value you want use if and elif

def right_color_checker():
  loop()
  if red > 12000 and blue < 7000 and green <7000:
    return("red")
  elif blue >12000 and green < 7000 and red < 7000:
    return("blue")
  elif blue >10000 and green > 10000 and red > 10000:
    return("n/a")


def left_color_checker():
  loop()
  if red > 12000 and blue < 7000 and green <7000:
    return("red")
  elif blue >12000 and green < 7000 and red < 7000:
    return("blue")
  elif blue >10000 and green > 10000 and red > 10000:
    return("n/a")

# what the robot does as specified values, for the last line, have to make it absed on which color sensor is reading that

def straight_line_following():
   left_co = left_color_checker()
   right_co = right_color_checker()
   left_co() # might not need dependeding on if teh variabel run regardless when entering the chekcing system, but can add a loop to continously run the pervious functions
   right_co()
   if left_co == right_co and left_co == blue:
      drivetrain.forward()
   elif left_co == right_co and left_co == red:
      drivetrain.stop()
   elif left_co != right_co and (left_co == n/a or right_co == n/a):   
     if left_co == n/a:
       drivetrain.right()
     if right_co == n/a:
       drivetrain.left()
     elif left_co= n/a and right_co == n/a
       drivetrain.stop()
# follwoig taped path 

      
  
  
