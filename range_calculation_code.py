"""
Stuff.
More Stuff
Spam
Green eggs and ham.

WE are going to do a range calculation.
"""

import math

gravity_m_per_sec_squared = 9.807
initial_velocity = 20
angle_in_degrees = 40
range = initial_velocity * initial_velocity\
 * math.sin(math.radians(2 * angle_in_degrees)) / gravity_m_per_sec_squared
print('our range', range)
