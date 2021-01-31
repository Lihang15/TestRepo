#coding=UTF-8
#字典
#键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
dict = {'a': 1, 'b': 2, 'b': 3}
print(dict['b'])
print(dict)

#2 修改字典
#添加字典元素
dict['h'] = 4
print(dict)

#删除字典，能删除单一的元素 也能清空字典
del dict['a']
print(dict)

del dict  #删除字典
print(dict)

# dict.clear() #清空所有条目
# print(dict)

#键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行,
# dict={['hh']:2,('tup'):3,'rrt':4}
# print(dict)
#运行以上代码出现error：TypeError: unhashable type: 'list'

dict = {('tup'): 3, 'rrt': 4}
print(dict)

print(dict.copy())  #浅拷贝
print(dict.get('tup'))  #返回指定key的值
print(dict.items())  #以列表返回所有可遍历的(key，value)元素数组
print(dict.keys())  #以列表返回所有的key
print(dict.values())  #以列表返回所有的value
print(dict.pop('tup'))  #删除指定key的value
print(dict.popitem())  #返回并删除字典中最后一对键值对
# dict1={('tup'):3,'rrt':4}
# dict2={'j':8,3:'u'}
# dict3=dict1.update(dict2)
# print(dict1.update(dict2))
# print(dict3)
