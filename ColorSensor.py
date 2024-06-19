import RPi.GPIO as GPI1
from time import time, sleep


# defs the setup for the left color sensor program
def left_setup():
  GPI1.setmode(GPI1.BCM)
  GPI1.setup(lsignal,GPI1.IN, pull_up_down=GPI1.PUD_UP)
  GPI1.setup(ls2,GPI1.OUT)
  GPI1.setup(ls3,GPI1.OUT)
  print("\n")

# defining the rgb values and what each value represents for the left color sensor
def l_loop():
  temp = 1
  while(1):  

    GPI1.output(ls2,GPI1.LOW)
    GPI1.output(ls3,GPI1.LOW)
    sleep(0.3)
    start = time()
    for impulse_count in range(lNUM_CYCLES):
      GPI1.wait_for_edge(lsignal, GPI1.FALLING)
    duration = time() - start 
    red  = lNUM_CYCLES / duration   
   
    GPI1.output(ls2,GPI1.LOW)
    GPI1.output(ls3,GPI1.HIGH)
    sleep(0.3)
    start = time()
    for impulse_count in range(lNUM_CYCLES):
      GPI1.wait_for_edge(lsignal, GPI1.FALLING)
    duration = time() - start
    blue = lNUM_CYCLES / duration
    
    GPI1.output(ls2,GPI1.HIGH)
    GPI1.output(ls3,GPI1.HIGH)
    sleep(0.3)
    start = time()
    for impulse_count in range(lNUM_CYCLES):
      GPI1.wait_for_edge(lsignal, GPI1.FALLING)
    duration = time() - start
    green = lNUM_CYCLES / duration

def left_color_checker():
  left_setup()
  l_loop()
  if red > 12000 and blue < 7000 and green <7000:
    return("1.0")
  elif blue >12000 and green < 7000 and red < 7000:
    return("2.0")
  elif blue >10000 and green > 10000 and red > 10000:
    return("0.0")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
# values are <7000 and >12000 -> for the RGB value you want use if and elif

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#right color sensor setup
def right_setup():
  GPI1.setmode(GPI1.BCM)
  GPI1.setup(rsignal,GPI1.IN, pull_up_down=GPI1.PUD_UP)
  GPI1.setup(rs2,GPI1.OUT)
  GPI1.setup(rs3,GPI1.OUT)
  print("\n")

# defining the rgb values and what each value represents for right color sesnor
def r_loop():
  temp = 1
  while(1):  

    GPI1.output(rs2,GPI1.LOW)
    GPI1.output(rs3,GPI1.LOW)
    sleep(0.3)
    start = time()
    for impulse_count in range(rNUM_CYCLES):
      GPI1.wait_for_edge(rsignal, GPI1.FALLING)
    duration = time() - start 
    red  = rNUM_CYCLES / duration   
   
    GPI1.output(rs2,GPI1.LOW)
    GPI1.output(rs3,GPI1.HIGH)
    sleep(0.3)
    start = time()
    for impulse_count in range(rNUM_CYCLES):
      GPI1.wait_for_edge(rsignal, GPI1.FALLING)
    duration = time() - start
    blue = rNUM_CYCLES / duration
    
    GPI1.output(rs2,GPI1.HIGH)
    GPI1.output(rs3,GPI1.HIGH)
    sleep(0.3)
    start = time()
    for impulse_count in range(rNUM_CYCLES):
      GPI1.wait_for_edge(rsignal, GPI1.FALLING)
    duration = time() - start
    green = rNUM_CYCLES / duration

def right_color_checker():
  right_setup()
  r_loop()
  if red > 12000 and blue < 7000 and green <7000:
    return("1.0")
  elif blue >12000 and green < 7000 and red < 7000:
    return("2.0")
  elif blue >10000 and green > 10000 and red > 10000:
    return("0.0")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# what the robot does as specified values, for the last line, have to make it based on which color sensor is reading that

def straight_line_following():
   left_co = int(left_color_checker())
   right_co = int(right_color_checker())
  
   if left_co == right_co and left_co == 2:
      drivetrain.forward()
   elif left_co == right_co and left_co == 1:
      drivetrain.stop()
   elif left_co != right_co and (left_co == n/a or right_co == n/a):   
     if left_co == 0:
       drivetrain.right()
     elif right_co == 0:
       drivetrain.left()
     elif left_co= 0 and right_co == 0
       drivetrain.stop()
# follwoig taped path 

        endprogram()
