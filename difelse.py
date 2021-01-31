#条件语句 if else
a=10
b=10
c=20

if (a==b)and(a==c):
    print("a==b==c")
elif (a==b)or (a==c):
    print("a==b or a==c")
elif (a is not c) or (a is not b):
    print("a not c or a is b")
else:
    print("else")