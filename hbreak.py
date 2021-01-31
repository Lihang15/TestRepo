#break  continue

for letter in 'python':
    if(letter == 'h'):
        break
        print(" n ")
    print("%s" %letter)
print("end")


for letter in 'python':
    if(letter == 'h'):
        continue
        print(" n ")
    print("%s" %letter)
print("end")


i=1
for num in range(1,10):
    for nu in range(12,18):
        print("%d : %d :%d "%(i,num,nu))
        i=i+1

