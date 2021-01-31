#coding=UTF-8
#日期和字典 时间戳
import time
tick = time.time()
print(tick)

localtime = time.localtime(time.time())
print(localtime)

#获取格式化的时间
#你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

import time
#我们可以使用 time 模块的 strftime 方法来格式化日期
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

#月历
#Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
import calendar
print(calendar.month(2021, 1))
