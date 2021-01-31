#coding=UTF-8
#斐波那契数列
print("-----1---")
a, b = 0, 1
while (b < 10):
    print(b)
    a, b = b, a + b

print("-----2---")
a = 0
b = 1
while (b < 10):
    print(b)
    m = a
    a = b
    b = m + b

print("-----3---")
#关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符，实例如下：
a = 0
b = 1
while (b < 1000):
    print(b, end=',')
    a, b = b, a + b
