#while循环
numbers=[12,19,37,10,14]
add=[]
odd=[]
length=len(numbers)
while(length>0):
    value=numbers[length-1]
    print("1.value: %d" %(value))
    if(value % 2 ==0):
        add.append(value)
        print("2.value: %d" %(value))
    else:
        odd.append(value)
        print("3.value: %d" %(value))
    length=length-1
print("numbers: %s" %(numbers))


#使用pop函数
numbers=[12,19,37,10,14]
add=[]
odd=[]
length=len(numbers)
while(length>0):
    value=numbers.pop()
    print("1.value: %d" %(value))
    if(value % 2 ==0):
        add.append(value)
        print("2.value: %d" %(value))
    else:
        odd.append(value)
        print("3.value: %d" %(value))
    length=length-1
print("numbers: %s" %(numbers))
print("--------------------------1----------------------")


#continue break ; while else
#coding=UTF-8
tuple=("1","hhh","2","9","汉语")
list=[1,34,6,8,9,11]
daleg=len(tuple)

length=len(list)
num=list[length-1]

flag=1
while(daleg>0 ):

    while(flag):
        num=list[length-1]
        if(length>0):
            if(num % 2 ==0):
                print("num: %d" %num)
                length=length-1
            else:
                 print("num%2 !=0")
                 print("num: %d" %num)
                 length=length-1
                 continue
                 print("i am after continue")
        else:
            print("length=6,break")
            flag=0
            break
            print("already break")

    daleg=daleg-1
    data=tuple[daleg]   
    print("data: %s" %data)     
else:
    print("tuple length==5")

