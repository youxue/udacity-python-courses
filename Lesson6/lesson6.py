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

