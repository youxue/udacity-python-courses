# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:53:38 2020

@author: WEN
"""

def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)
    # Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
    # 断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况
    
    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)
    
    print("All tests passed!")

if __name__ == '__main__':
    main()
    
'''
每当我们运行此类脚本时，Python 实际上会为所有模块设置一个特殊的内置变量 __name__
当我们运行脚本时，Python 会将此模块识别为主程序
并将此模块的 __name__ 变量设为字符串 "__main__"
对于该脚本中导入的任何模块，这个内置 __name__ 变量会设为该模块的名称
因此，条件 if __name__ == "__main__"会检查该模块是否为主程序。
'''