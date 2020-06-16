# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 23:11:00 2020

@author: WEN
"""

#Part 3 Function
#quiz 1
def population_density(population, land_area):
    return population/land_area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))
print("\n")


#Part 3 quiz 2
def readable_timedelta(days):
    week = days // 7
    day = days % 7
    return "{} week(s) and {} day(s).".format(week, day)

# test your function
print(readable_timedelta(10))
print("\n")


# Part 6 Variable Scope
#Python 不允许函数修改不在函数作用域内的变量。但是原则仅适用于整数和字符串。
#列表、字典、集合、类中可以在子程序（子函数）中通过修改局部变量达到修改全局变量的目的。
#例如下面的 Code 将返回 UnboundLocalError

#egg_count = 0

#def buy_eggs():
    #egg_count += 12 # purchase a dozen eggs

#buy_eggs()


#Part 8 DocScring
#在 function 定义行的下面，是 function 的多行注释。用 """ """ 开始和结束。
#注释第一行解释 function 的作用。如果function 简单可以只写这一行
def population_density(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT: 
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area



#Part 11 Lambda Expressions 用于创建匿名函数
#适合快速创建在代码中以后不会用到的函数。尤其对高阶函数或将其他函数作为参数的函数
def multiply(x, y):
    return x * y

#可简写为：
double = lambda x, y: x * y




#Part 12 quiz 1
#map() 是一个高阶内置函数，接受函数和可迭代对象作为输入，并返回一个将该函数应用到可迭代对象的每个元素的迭代器。
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

#用 lambda 重写：
averages = list(map(lambda num_list : sum(num_list) / len(num_list), numbers))
print(averages)
print("\n")



#Part 12 quiz 2
#filter() 是一个高阶内置函数，接受函数和可迭代对象作为输入，并返回一个由可迭代对象中的特定元素（该函数针对该元素会返回 True）组成的迭代器。
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)

#用 lambda 重写：
short_cities = list(filter(lambda name : len(name) < 10, cities))
print(short_cities)
print("\n")