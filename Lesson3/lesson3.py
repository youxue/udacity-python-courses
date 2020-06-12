# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:06:04 2020

@author: jywen
"""

# Part 3 quiz 1
sum=23+32+64
print(sum/3)
print("\n")



#Part 3 quiz 2
# Fill this in with an expression that calculates how many tiles are needed.
print(9*7+5*7)

# Fill this in with an expression that calculates how many tiles will be left over.
print(17*6 - (9*7+5*7))
print("\n")



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
print("\n")



#Part 7
x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0
print(type(x))
print(type(y))
print(.1 + .1 + .1 == .3)
print("\n")



#Part 9 quiz 1
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density > rio_de_janeiro_pop_density)
print("\n")



#Part 11
word = "word"
print(word*5)
print(len(word))
this_string = 'Simon\'s skateboard is in the garage.'
print(this_string)
first_word = 'Hello'
second_word = 'There'
print(first_word + ' ' + second_word)
print("\n")



#Part 12 quiz 1
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Kinari accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

print(username + " accessed the site " + url + " at " + timestamp + ".")
print("\n")



#Part 12 quiz 2
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"
full_name = given_name + " " + middle_names + " " + family_name
name_length = len(full_name)
print(full_name)
print(name_length)
print(len(given_name + middle_names + family_name) + 2)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
print("\n")


#Part 14 quiz 1
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
print("This week's total sales: " + str(total_sales))
print("\n")


#Part 16 quiz 1
# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# and try them out here

text="The COVID-19 coronavirus pandemic"
print("Convert text to lower cases: " + text.lower())
print(text.find("virus"))

text2 = "There were averate {0} people died per day in the past {1} days"
print(text2.format(3,7))
print("\n")


#Part 17 list
lst_of_random_things = [1, 3.4, 'a string', True]
print(lst_of_random_things[1:2])
print(5 not in [1, 2, 3, 4, 6])
print('isa' in 'this is a string')
print("\n")


#Part 18 quiz 1
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month

num_days = days_in_month[month-1]
print(num_days)
print("\n")


#Part 18 quiz 2
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
# TODO: Modify this line so it prints the last three elements of the list

print(eclipse_dates[-3:])
print("\n")



#Part 19 list join & append
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
print(len(new_str))

letters = ['a', 's', 'c', 'd']
letters.append('z')
print(letters)
print(max(letters))
print(min(letters))
print(sorted(letters)) #sorted doesn't change the original list
print(letters)
print("\n")



#Part 20 
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))
print("\n")


#Part 21 tuples 元组
#有序对象集合，对象不能编辑， 通常于紧凑的对象对儿或者快速存取类似list一样的值
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])
print(type(location))

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

length, width, height = 52, 40, 100
print("The dimensions are {} {} {}".format(length, width, height))
print("\n")


#Part 23 Set 集合
# Mutable Unordered Collections of Unique Elements
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

fruit = {"apple", "banana", "orange", "grapefruit"} # define a set
print("watermelon" in fruit) # check for element
fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop()) # remove a random element
print(fruit)

#可以对集合轻松地执行 union、intersection 和 difference 等方法，并且与其他容器相比，速度快了很多。
print("\n")


#Part 




