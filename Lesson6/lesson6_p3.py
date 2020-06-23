# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:53:11 2020

@author: WEN
"""

'''
import 语句会创建一个模块对象。模块是包含定义和语句的 Python 文件。要访问导入模块中的对象，需要使用点记法。

每当我们运行此类脚本时，Python 实际上会为所有模块设置一个特殊的内置变量 __name__
当我们运行脚本时，Python 会将此模块识别为主程序
并将此模块的 __name__ 变量设为字符串 "__main__"
对于该脚本中导入的任何模块，这个内置 __name__ 变量会设为该模块的名称
因此，条件 if __name__ == "__main__"会检查该模块是否为主程序。

'''

import other_functions as of

scores = [88, 92, 79, 93, 85]

mean = of.mean(scores)
curved = of.add_five(scores)

mean_c = of.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, "New Mean:", mean_c)

print(__name__)
print(of.__name__)