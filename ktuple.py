#元组,元组中元素值不允许被修改
#元组中只包含一个元素时，需要在元素后面添加逗号
tuple0=(12,)
print("%s " %(tuple0))

#2 元组相加
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3=tup1 + tup2
print(tup3)

#删除元组
tup4=("123",33.0,"gg",'hhh')
#del tup4
print(tup4)
#s删除后会报错：NameError: name 'tup4' is not defined

#乘
print(tup4*4)

#迭代
for x in tup4:
    print(x)
#判断元素是否在元组中
print(3 in tup4)

#索引 与列表相同

#任意无符号的对象，以逗号隔开，默认为元组，如下实例：
z,y=1,2
m='q',5,'qw','tt','ui','i8','5f'
print(z,y)
print(m)

#将列表转化为元组
list1=['hello','world','yuo']
tuple(list1)
print(list1)

#cmp,操作同list
import operator
#print(operator.--(tup1,tup3))
