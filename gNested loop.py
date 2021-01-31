#嵌套循环 素数

# public static void test2() {
#  2         int i, j;
#  3         for (i = 2; i <= 100; i++) {
#  4             for (j = 2; j < i; j++) {
#  5                 if (i % j == 0)
#  6                     break;
#  7             }
#  8             if (j >= i)
#  9                 System.out.println(i);
# 10         }
# 11     }


#coding=UTF-8
for i in range(2,100):
    for x in range(2,i):
        if(i % x ==0):
            break
    else:
        print("i= %d" %i)

#算法思想：按顺序取2-100之间的数i，
#i%x 如果有==0的情况则直接判断其不为质数，比如9%3 9%6，当判断9%3==0时直接break,根本不用判断9%6，
#有一个非己因数就说明是非质数，
#直接判断下一个数，i++  比如10
#那么i%x ！=0 且x++以后不小于i了，那么此时，说明i=x，这个数x就是i它本身，即证明他是质数