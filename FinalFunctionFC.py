import gpiozero
from time import sleep, time
import RPi.GPIO as GPI1 # for color sensor program
import busio # for lidar sensor
import board # for lidar sensor
import adafruit_lidarlite # for lidar sensor
import adafruit_ht16k33.segments # for lidar sensor
#the functions in this code can be found on te other files across te github

left_co = int(left_color_checker())
right_co = int(right_color_checker())

def ovrfunc():
    if on_button is pressed:
      drivetrain.forward
      sleep(0.5)
      drivertrain.right
      sleep(0.5)
      #the first 4 lines state that if the button is pressed the the robot will get out of the hub, move forward for 0.5 seconds, stop, trun left 
      while left_co != 2:
        drivertrain.forward
        #the robot will go forward until the left_color sensor reads blue can be chnaged to green which is 3.0 and needs to be added on to the color checker function
      if left_co == 2:
        while right_co != 2:
          drivetrain.left
        # once left color sensor reads blue the robot will turn right until the right color sensor also reads blue
      while True:
        striaght_line_following()
        #cross references the color sensors to make sure rover is going straight, via integer values
        dist_checker()
        #references distance set in other docs to make sure robot is not too close to the wall
        if button_off():
          exit()
          #shut down program

# running the acctual code after full function define
run = bool('dhir')
while run == True:
  ovrfunc()
  
    
  
        
      
