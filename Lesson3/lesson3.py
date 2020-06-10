# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:06:04 2020

@author: jywen
"""

# Part 3 quiz 1
sum=23+32+64
print(sum/3)



#Part 3 quiz 2
# Fill this in with an expression that calculates how many tiles are needed.
print(9*7+5*7)

# Fill this in with an expression that calculates how many tiles will be left over.
print(17*6 - (9*7+5*7))



#Part 5 quiz 1
#4.445e8 is 4.445*10 ** 8
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff

# add the rainfall variable to the reservoir_volume variable

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm

# decrease reservoir_volume by 5% to account for evaporation

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.

# print the new value of the reservoir_volume variable

rainfall *=  .9
reservoir_volume += rainfall
reservoir_volume *= 1.05
reservoir_volume -= reservoir_volume * 0.05
reservoir_volume -= 2.5e5
print(int(reservoir_volume))



