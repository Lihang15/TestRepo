#for循环
for num in "python":
    print("num: %s" %num)

fruit=["apple", "pear", "hello"]
for index in range(len(fruit)):
    print("fruit: %s" %fruit[index])


for value in range(10,20):
    for i in range(1,value):
        print("value: %d" %value)
        print("i: %d" %i)
        break


for data in range(10,20):
    print("data: %d" %data)
