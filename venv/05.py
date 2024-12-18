#题目:给定一个数,将其反序输出
#姓名:武洪斌

print("请输入一个数字")
num = int(input())

n = len(str(num))
list = []
for i in range(n):
    temp = num % 10
    num = num //10
    list.append(temp)
    print(list[i],end = "")