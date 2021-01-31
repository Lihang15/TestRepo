#!/usr/bin/pyhton3
#Filename:Rtest.py
import Rmodule

Rmodule.print_fun("world")

import sys
print(sys.path)

#from … import 语句
#Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：
# 斐波那契(fibonacci)数列模块
from Rmodule import *
print(fib(10))

from Rmodule import fib, fib2
print(fib2(20))
print(fib(10))

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')
