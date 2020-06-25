# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 23:09:36 2020

@author: WEN
"""

#标准库 https://pymotw.com/3/; https://docs.python.org/3/library/index.html
#推荐模块：
'''
csv：对于读取 csv 文件来说非常便利
collections：常见数据类型的实用扩展，包括 OrderedDict、defaultdict 和 namedtuple
random：生成假随机数字，随机打乱序列并选择随机项
string：关于字符串的更多函数。此模块还包括实用的字母集合，例如 string.digits（包含所有字符都是有效数字的字符串）。
re：通过正则表达式在字符串中进行模式匹配
math：一些标准数学函数
os：与操作系统交互
os.path：os 的子模块，用于操纵路径名称
sys：直接使用 Python 解释器
json：适用于读写 json 文件（面向网络开发）

'''

#Part 23 quiz 1 & 2
import math
import random
print(math.exp(3))

word_file = "/udacity-python-courses/words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
# def generate_password():
#     return ''.join(random.sample(word_list,3))

# test your function
print(generate_password())
print("\n")


#Part 25
#从一个模块中导入几个单独对象
#from module_name import first_object, second_object


#Part 27 第三方库
'''
pip 是在 Python 3 中包含的软件包管理器，它是标准 Python 软件包管理器，但并不是唯一的管理器。
另一个热门的管理器是 Anaconda，该管理器专门针对数据科学。
命令：ip install package_name
程序员经常会在叫做 requirements.txt 的文件中列出项目的依赖项。例如：
beautifulsoup4==4.5.1
bs4==0.0.1
使用 pip 一次性安装项目的所有依赖项。命令：
ip install -r requirements.txt
实用的第三方软件包:
IPython - 更好的交互式 Python 解释器
requests - 提供易于使用的方法来发出网络请求。适用于访问网络 API。
Flask - 一个小型框架，用于构建网络应用和 API。
Django - 一个功能更丰富的网络应用构建框架。Django 尤其适合设计复杂、内容丰富的网络应用。
Beautiful Soup - 用于解析 HTML 并从中提取信息。适合网页数据抽取。
pytest - 扩展了 Python 的内置断言，并且是最具单元性的模块。
PyYAML - 用于读写 YAML 文件。
NumPy - 用于使用 Python 进行科学计算的最基本软件包。它包含一个强大的 N 维数组对象和实用的线性代数功能等。
pandas - 包含高性能、数据结构和数据分析工具的库。尤其是，pandas 提供 dataframe！
matplotlib - 二维绘制库，会生成达到发布标准的高品质图片，并且采用各种硬拷贝格式和交互式环境。
ggplot - 另一种二维绘制库，基于 R's ggplot2 库。
Pillow - Python 图片库可以向你的 Python 解释器添加图片处理功能。
pyglet - 专门面向游戏开发的跨平台应用框架。
Pygame - 用于编写游戏的一系列 Python 模块。
pytz - Python 的世界时区定义。
'''

#Part 28 在解释器中进行实验 & Ipython
'''
IPython
实际上有一个代替默认 python 交互式解释器的强大解释器 IPython，它具有很多其他功能。

Tab 键补充完整
?：关于对象的详细信息
!：执行系统 shell 命令
语法突出显示
https://ipython.org/ipython-doc/3/interactive/tutorial.html
'''


#Part 29 在线资源
'''
python官方教程： https://docs.python.org/3/tutorial/
python 语言和库参考资料：https://docs.python.org/3/index.html
第三方库文档：https://readthedocs.org/
stackOverflow: https://stackoverflow.com/
Bug 跟踪器 - 有时候，你可能会遇到非常罕见的问题或者非常新的问题，没有人在 StackOverflow 上提过。
例如，你可能会在 GitHub 上的 bug 报告中找到关于你的错误的信息。
这些 bug 报告很有用，但是你可能需要自己开展一些工程方面的研究，才能解决问题。
'''



