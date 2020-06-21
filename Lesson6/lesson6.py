# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:17:35 2020

@author: WEN

Topic: Script 脚本
"""

"""
脚本与一般程序的主要区别在于是否编译。
相对于程序而言，脚本更加随性。写完了脚本，直接就可以在某种具有解释功能的环境中运行。
而非脚本语言（编译语言），比如 C、Java 语言。
我们需要通过编译（Compile）和链接（link）等步骤，生成可执行文件。
然后通过可执行文件在计算机上运行。
"""

#Part 8 quiz 1
how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)
print("\n")


#Part 9
name = input("Enter a name:")
print("Hello " + name.title())

num = int(input("Enter an integer:"))
print("hello: " * num)

#使用内置函数 eval 将用户输入解析为 Python 表达式。该函数会将字符串评估为一行 Python 代码。
result = eval(input("Enter an expression: "))
print(result)

print("\n")


#Part 10 quiz 1
names = input("Enter names separated by commas:").title().split(",")
assi_counts = input("Enter assignment counts separated by commas:").split(",")
grades = input("Enter grades separated by commas:").split(",")
for name, assi_count, grade in zip(names, assi_counts, grades):
    poten_grade = int(assi_count) * 2 + int(grade)
    print("Hi {}, \n".format(name))
    print("This is a reminder that you have {} assignments left to \
          submit before you can graduate. Your current Grade is {} \
          and can increase to {} if you submit all assignments before \
              the due date.\n".format(assi_count, grade, poten_grade))
print("\n")



#Part 14 Exception
while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("That\'s not a valid number!")
    except KeyboardInterrupt:
        print("\nNo input taken")
        break
    finally:
        print("\nAttempted Input\n") #Finally 无论前面执行的如何最后都会执行，即使程序被打断或者 break
# 还有这种写法
# except (ValueError, KeyboardInterrupt):
    # some code
print("\n")


#Part 15 quiz 1
def create_groups(items, num_groups):
    try:
        size = len(items) // num_groups
    except ZeroDivisionError:
        print("WARNING: Returning empty list. Please use a nonzero number.")
        return []
    else:    
        groups = []
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
        return groups
    finally:
        print("{} groups returned.".format(num_groups))

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))
    print("WARNING: Returning empty list. Please use a nonzero number.")
