# distance sesnor code 

f_dis_sensor = gpiozero.DistanceSensor(#Gpiozero number, second number, max_distance = 3, threshold_distance = 0.2) front distance sensor
l_dis_sensor = gpiozero.DistanceSensor(#Gpiozero number, second number, max_distance = 3, threshold_distance = 0.2) left distance sensor
r_dis_sensor = gpiozero.DistanceSensor(#Gpiozero number, second number, max_distance = 3, threshold_distance = 0.2) right distance sensor
b_dis_sensor = gpiozero.DistanceSensor(#Gpiozero number, second number, max_distance = 3, threshold_distance = 0.2) back distance sensor

def distance_checker(): 
  while f_dis_sensor.in_range:
    if l_dis_sesnor.in_range:
      drivertrain.right
    elif r_dis_sensor.in_range
      drivertrain.left
    elif l_dis_sensor.in_range && r_dis_sensor.in_range:
      while l_dis_sensor.in_range && r_dis_sensor.in_range:
        drivetrain.backward
        b_dis_sensor.when_in_range = drivertain.stop 
    elif
      drivetrain.stop
  
def move_until_w/o_color:
  while f_dis_sensor.out_of_range:  
    drivetrain.forward
  
  #dis_sensor.when_in_range = drivetrain.stop
  #dis_sensor.when_out_of_range = drivetrain.forward
