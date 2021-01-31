#第二节变量类型

a,b,c=1,2,"hello world"
print(a,b,c)
print("-----------------------1-----------------------------")


var1 =[1,2,3,3,4]
var2= 'start'
#删除变量
del var1,var2
#print(var1)
#print(var2)
print("check if delete or not")
print("-----------------------2-----------------------------")

#字符串索引和获取
string="hello world！"
var="1,2,3,3,4"

#searching;-12 -> -1 ;0->11
print(string)
print(string[:])
print(string[0:])
print(string[0:11])
print(string[-12:-1])
print(string+var)
print(string*2)
print("-----------------------3.1-----------------------------")
#getting;
print(string[1:7])
print(string[0:7])
print(string[1:])
print(string[:])
print(string[-12:-1])
print(string[-12:])
print(string[:])
print("------------------------3.2----------------------------")

#Python 列表截取可以接收第三个参数，参数作用是截取的步长
print(string[-11:-2:7])
print("-----------------------3.3-----------------------------")

#list
list=["123","abcd",'h']
tinylist=[1,2,3,4,5]
print(list+tinylist)
print("-----------------------3.4-----------------------------")


#元组是另一个数据类型，类似于 List（列表）。元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
list=["123","abcd",'h']
list=[1,2,3,4,5]
list[2]='h'
print(list);print("list is replaced and assigned successfully")
tuple=("123456789",'hello')
tuple=('world')
# tuple[2]='9' str' object does not support item assignment,元组不支持二次赋值
print(tuple)
tinxtuple=("123456789",'hello')
tinytuple=('1','6','10')
print (tinxtuple + tinytuple )
print("-----------------------3.5-----------------------------")


#字典用"{ }"标识。字典由索引(key)和它对应的值value组成。字典当中的元素是通过键来存取的，而不是通过偏移存取
dictory={}
dictory['one']="this is a dictory"
dictory[3]="this is adictory too"
tinydictory={1:'first',2:'second',3:'third',4:'four',5:'five'}

print(dictory['one'])
print(dictory[3])
print(dictory)
print(dictory.keys())
print(dictory.values())
print(tinydictory.keys())
print(tinydictory.values())
print("-----------------------3.6-----------------------------")