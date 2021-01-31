#coding=UTF-8
#set集合，集合（set）是一个无序的不重复元素序列
#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

set()
print(set)

#去重功能
backet = {'apple', 'pear', 'wine', 'apple', 'pear'}
print(backet)
print('apple' in backet)  #true

a = set('arbrbacadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)  #a里有，b里没有的
print(b - a)  #b里有，a里没有的
#print(a + b) 不支持
print(a & b)  #a和b都有的元素
print(a | b)  #a或b里包含的
print(a ^ b)  #不同时包含a b里的元素

#集合添加元素
a.add("hello")
a.add('abbc')
print(a)

#还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：x 可以有多个，用逗号分开。

a.update({1, 3, 'h', "good"}, [1, 4])  #重复元素不进行操作
print(a)

#移除元素, 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
#a.remove('f')
a.remove('a')
print(a)
#此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：
a.discard("f")
print(a)  #直接输出原集合

#我们也可以设置随机删除集合中的一个元素，语法格式如下：
x = a.pop()
print(x)  #set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。

#长度
#拷贝集合
print(len(a))
y = a.copy()
print(y)

#判断元素是否在集合中存在
print('m' in a)
print('b' in a)

#清空集合
m = a.clear()
print(a)
