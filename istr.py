
#str
string ="wealthy"
str=string[0:7]+" hello world"
print(str)


#定义一个字符串AaBbCc将此字符串字符全部为小写输出/大写输出/原字符串逆序/字符串替换/字符串分割
#coding=UTF-8

#1
str='AaBbCc'
print("全小写： %s" %(str.lower()))

#2
str='AaBbCc'
print("全大写： %s" %(str.upper()))

#3
str='AaBbCc'
listr =list(str)
stt=listr.reverse()
#print("stt: %s" %stt)
print("listr: %s" %listr)
print("逆序输出：" + ''.join(listr)) ##join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
print('*'.join(listr))
#4
str='AaBbCc'
print("替换后的字符串为： %s" %(str.replace("Bb","ha")))

#5
str='Aa,Bb,Cc'
print("分割后的字符串为： %s" %(str.split(',')))


#6 一个个字符顺序输出
stb='AaBbCc'
for i in stb:
    print("%s" %(i))

#7一个个字符逆序输出
stb ='aAbBcC'
list11=list(stb)
list11.reverse()
print("%s" %list11)
for i in list11[0:6]:
    print("%s" %(i))


