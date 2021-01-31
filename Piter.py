#coding=UTF-8
#迭代器和生成器
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器：
# print("-----1---\n")
# list1 = ['hello', 1, 6, 10, 'fg']
# it1 = iter(list1)
# for x in it1:
#     print(x, end='  ')

# print("\n-----2---")
# list2 = ['hello', 1, 6, 10, 'fg']
# it2 = iter(list2)
# import sys
# while True:
#     try:
#         print(next(it2))
#     except StopIteration:
#         sys.exit()

print("\n-----3---")


#self 相当于 this； def是表示这个函数属于这个类
class Piter:
    def __iter__(self):  #注意： iter前的-是两个-  __
        self.a = 1
        return self

    def __next__(self):
        b = self.a
        self.a += 1
        return b


myclass = Piter()  #myclass是一个对象，piter是空构造函数
myiter = iter(myclass)

i = 1
while (i < 6):
    print(next(myiter))
    i = i + 1
