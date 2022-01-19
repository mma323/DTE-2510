#Programmet genererer et tilfelding punkt innenfor en sirkel med
#sentrum i origo og radius 5

import math             #Brukes for sinus og cosinus 
import random as rdm    #Hentes for bruk av random.random()

radius = 5

#Punktet er mellom 0 og radius enheter unna sentrum av sirkelen
distance_from_centre_of_circle_to_point = float(rdm.random() * radius)
#Vinkelen i en sirkel kan være mellom 0 og 2pi
angle_between_distance_and_x_axis       = float(rdm.random() * 2 * math.pi)

#Et punkt innenfor en sirkel er gitt ved (dcos(a), dsin(a)), der d er avstand 
#fra punkt til sentrum og a er vinkelen mellom x-akse og avstanden
x_value_of_point = (distance_from_centre_of_circle_to_point * 
                    math.cos(angle_between_distance_and_x_axis))
y_value_of_point = (distance_from_centre_of_circle_to_point *
                    math.sin(angle_between_distance_and_x_axis))

print(f"The point is ({x_value_of_point}, {y_value_of_point}) and its distance"
      f" to the centre is {distance_from_centre_of_circle_to_point}")

