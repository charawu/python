#题目:求三位数各数字之和
#姓名:武洪斌

while True:
    print("请输入任意三位数")
    num = str(input())
    if len(num) == 3:
        break

list1 = list(num)
print("各数字之和分别为:",int(list1[0]) + int(list1[1]),",",int(list1[1])+ int(list1[2]),",",int(list1[0]) + int(list1[2]))