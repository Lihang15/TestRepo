#list  append函数,用来添加元素
list=[]
list.append("hello")
list.append("world")
print("list: %s"%list)#hello world

#list del删除元素
del list[1]
print("list: %s"%list)#[hello]

del list[0:1]
print("list: %s"%list)#[]

L = ['Google', 'Runoob', 'Taobao']#-3 -2 -1
print("list: %s"%L[2])#Taobao
print("list: %s"% L[-2])#Runoob
print("list: %s"%L[1:])#Runoob Taobao

#cmp(list1,list2),a的ascll码值a最小
list1=['hello','world']
list2=['about','world']
list3=['hello','about']
list4=['hello','world']

import operator
if(operator.gt(list1,list2)):
    print("list1 大于list2")
    print("operator.eq(list1,list2): %s",operator.gt(list1,list2))
if(operator.ge(list1,list2)):
    print("list1 大于等于list2")
    print("operator.eq(list1,list2): %s",operator.ge(list1,list2))
if(operator.lt(list1,list2)):
    print("list1 小于 list2")
    print("operator.eq(list1,list2): %s",operator.lt(list1,list2))
if(operator.le(list1,list2)):
    print("list1 小于等于list2")
    print("operator.eq(list1,list2): %s",operator.le(list1,list2))
if(operator.eq(list1,list2)):
    print("list1 等于list2")
    print("operator.eq(list1,list2): %s",operator.eq(list1,list2))
if(operator.ne(list1,list2)):
    print("list1 不等于list2")
    print("operator.eq(list1,list2): %s",operator.ne(list1,list2))

#明天写第2个列表元素
#mix min
print("%s " %max(list1))#world
print("%s " %min(list1))#hello

#list.append(obj) 在列表末尾添加新的对象
list1.append("you")
print("%s " %(list1))
#list.count(obj) #统计某个元素在列表中出现的次数
print("%s " %(list1.count("hello")))
#list.index(obj)从列表中找出某个值第一个匹配项的索引位置
print("%s " %(list1.index("hello")))
#list.insert(index, obj) 将对象插入列表,插在index位置，插入内容为obj
list1.insert(2,"hello")
print("%s " %(list1))
#list.pop([index=-1] )移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print("%s " %(list1.pop(-1)))
print("%s " %(list1))
#list.remove(obj) 移除列表中某个值的第一个匹配项
list1.remove('world')
print("%s " %(list1))
#list.reverse() 反向列表中元素
list2.reverse()
print("%s " %(list2))

# strr="hello"
# stt=list(strr)
# stt.reverse()
# print("%s ",stt)

#	list.sort(cmp=None, key=None, reverse=False)对原列表进行排序
list5=['ho','ab','tr','cc','po','ui']
list5.sort()
print("%s " %(list5))



