#题目：从键盘输入任意正整数n，找出最大的数字
#姓名：武洪斌

print("请输入任意正整数")
num = int(input())

list_num = []
for i in range(len(str(num))):
    o = num % 10
    num = num // 10

    list_num.append(o)

print(max(list_num))