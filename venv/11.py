#题目:输出字符金字塔
#姓名:武洪斌

#分析，输出总列数中空格数为n-(1~n),字符可以分两次，1.倒序，2.正序

print("请输入要输出列数")
n = int(input())

for i in range(1,n+1):
    print("1",end="")
    for j in range(41,i+41):
        print(chr(j),end="")