#coding=UTF-8
#遍历
#1 字典 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
print("-----1---\n")
dict = {1: 'hello', 2: "world", 3: 'pepper'}
for i, v in dict.items():  #item似乎是和类型有关
    print(i, v)

#2 序列 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
print("-----2---\n")
for j, b in enumerate(["hello", "pop", "uuu"]):
    print(j, b)

#同时遍历两个或更多的序列，可以使用 zip() 组合：

print("-----3---\n")
list1 = ['h', 'e', 'l', 'l', 'o']
list2 = ['w', 'o', 'r', 'l', 'd']
for n, m in zip(list1, list2):
    print(n, m)

#要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
print("-----4---\n")
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):  #集合是不重复的，只有一个apple
    print(f)

#要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
print("-----4---\n")
cellnum = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for k in reversed(cellnum):
    print(k)
