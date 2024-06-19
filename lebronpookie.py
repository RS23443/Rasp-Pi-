import gpiozero
from time import sleep


button_on = gpi0zero.Button(2)
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
define on(): 
  if button_on is pressed:
    robot.forward()
    sleep(5)
    robot.right()
    sleep(5)
    robot.left()
    sleep(5)
    robot.backward()
    sleep(5)
    
# off function, turns robo off
define off():
  if button_off is pressed:
    robot.stop()

define color_checker():
  
