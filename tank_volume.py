# To introduce the problem think to my neighbor who drives a tanker truck. The level indicator is down and he is worried because he does not know if he will be able to make deliveries. We put the truck on a horizontal ground and measured the height of the liquid in the tank.

# Fortunately the tank is a perfect cylinder and the vertical walls on each end are flat. The height of the remaining liquid is h, the diameter of the cylinder is d, the total volume is vt (h, d, vt are positive or null integers). You can assume that h <= d.

# Could you calculate the remaining volume of the liquid? Your function tankvol(h, d, vt) returns an integer which is the truncated result (e.g floor) of your float calculation.

import math

def tankvol(h, d, vt):
  radius = d/2
  if h == radius:
    return math.floor(vt/2)
  else:
    angle = math.acos((radius-h)/radius)
    slice_volume = ((angle*2)/(2*math.pi))*vt
    b = math.sin(angle)*radius
    triangle_area = b*(radius-h)
    area_of_tank = math.pi*radius**2
    length_of_tank = vt/area_of_tank
    triangle_volume = triangle_area*length_of_tank
    fuel_remaining = slice_volume-triangle_volume
    return math.floor(fuel_remaining)


print(tankvol(80,120,3500)) #returns 2478