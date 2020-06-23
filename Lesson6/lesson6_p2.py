# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 18:09:48 2020

@author: WEN
"""

#Part 18 File

f = open('/udacity-python-courses/testfile.txt', 'r')
#r，即只读模式。是模式参数的默认值。
file_data = f.read()
f.close()
print(file_data)

f = open('/udacity-python-courses/testfile.txt', 'a')
f.write("\nHello there!")
f.close()
# 以写入 ('w') 模式打开文件。
# 如果文件不存在，Python 将为你创建一个文件。
# 如果以写入模式打开现有文件，该文件中之前包含的所有内容将被删除。
# 如果你打算向现有文件添加内容，但是不删除其中的内容，可以使用附加 'a'

with open('/udacity-python-courses/testfile.txt', 'r') as f:
    file_data = f.read()
print(file_data)
#f 之能在缩进的代码块中使用。
#python 会在执行了缩进代码块后自动close file


#Part 19 quiz 1
# 如果向 .read() 传入整型参数，它将读取长度是这么多字符的内容，
# 输出所有内容，并使 'window' 保持在该位置以准备继续读取。

with open('/udacity-python-courses/testfile.txt') as f2:
    #读取两个字符
    file_data1 = f2.read()
    #读取一行
    file_data2 = f2.readline()


#Part 19 quiz 2
camelot_lines = []
with open("camelot.txt") as f:
    for line in f: #Python 的固定语法
        camelot_lines.append(line.strip())
        #line.strip()去掉行尾的换行符
print(camelot_lines)


#Part 19 quiz 3
def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    
    with open('/udacity-python-courses/'+ filename) as f:
        for line in f:
            line = line.strip()
            lineitem = line[:line.find(",")]
            cast_list.append(lineitem)
            # line_data = line.split(',')
            # cast_list.append(line_data[0])

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)


