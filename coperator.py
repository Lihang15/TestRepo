#第三节运算符
#基础运算符
a=10
b=20
c=a+b
print("c的值为：%d----------------------: %d" %(1,c))
c=a-b
print("c的值为：%d----------------------: %d" %(2,c))
c=a*b
print("c的值为：%d----------------------: %d" %(3,c))
c=b/a
print("c的值为：%d----------------------: %d" %(4,c))
c=a%b
print("c的值为：%d----------------------: %d" %(5,c))
c=a//b
print("c的值为：%d----------------------: %d" %(6,c))
c=a**b
print("c的值为：%d----------------------: %d" %(7,c))
print('\n')

#比较运算符
a=10
b=20
c=0
if a>b:
    print("a>b")
elif a<b:
    print("a < b")
elif a==b:
    perint("a==b")

if a != b:
    print("a != b")
print('\n')

#位运算符
a=60
b=13
c=0
print("a的二进制值为：: %s" %format(a,'b'))
print("a的八进制值为：: %s" %format(a,'o'))
print("a的十六进制值为：: %s" %format(a,'x'))
print("b的二进制值为：: %s" %format(b,'b'))
print("b的八进制值为：: %s" %format(b,'o'))
print("b的十六进制值为：: %s" %format(b,'x'))
c=a&b
print("c的值为：%d----------------------: %s" %(1,format(c,'b')))
c=a|b
print("c的值为：%d----------------------: %s" %(2,format(c,'b')))
c=a^b
print("c的值为：%d----------------------: %s" %(3,format(c,'b')))
c=~a
print("c的值为：%d----------------------: %s" %(4,format(c,'b')))
c=~b
print("c的值为：%d----------------------: %s" %(5,format(c,'b')))
c=a<<2
print("c的值为：%d----------------------: %s" %(6,format(c,'b')))
c=a>>2
print("c的值为：%d----------------------: %s" %(7,format(c,'b')))
c=b<<2
print("c的值为：%d----------------------: %s" %(8,format(c,'b')))
c=b>>2
print("c的值为：%d----------------------: %s" %(9,format(c,'b')))
print('\n')

#逻辑运算符 and;or;not
a=1  #(Ture)
b=False #(False)
c=a and b
if c:
    print("c的值为：%d----------------------: %s" %(1,c))
else:
    print("c的值为：%d----------------------: %s" %(1,c))

c=a or b
if c:
    print("c的值为：%d----------------------: %s" %(1,c))
else:
    print("c的值为：%d----------------------: %s" %(1,c))

c=not (a and b)
if c:
    print("c的值为：%d----------------------: %s" %(1,c))
else:
    print("c的值为：%d----------------------: %s" %(1,c))


#成员运算符 in; not in
# coding=UTF-8 
list=[1,2,3,4,5,6,7,8,9,10]
tuple=("h","abc","pod",'11','12')
dict={1:'yut',2:'13'}
a=2
b='abc'
c='u'
d=13
e=19


if (a in list):
    print("a in list")
elif((b in list)or(c in list)or(d in list)or(e in list)):
    print("a not in list")


if (a in tuple):
    print("a in tuple")
elif((b in tuple)or(c in tuple)or(d in tuple)or(e in tuple)):
    print("a not in tuple")

if (a in dict):
    print("a in dict")
elif((b in dict)or(c in dict)or(d in dict)or(e in dict)):
    print("a not in dict") 


if (b not in list):
    print("b not in list")
else:
    print("b in list")

print('\n')


#身份运算符 is；is not
a=10
b=20
c=10

if(a is b):
    print("a==b")
elif(a is c):
    print("a==c")
else:
    print("a is not b or c")

if (a is not b):
    print("a is not b")
else:
    print("a is b")

#is 与 == 区别：
#is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。
