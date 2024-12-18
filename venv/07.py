# 题目:输入5个数让其分别以从大到小输出和从小到大输出
# 姓名:武洪斌

list = []
n = 5
for i in range(n):
    print("请输入第", i + 1, "个数")
    list.append(int(input()))

while not list[0] < list[1] < list[2] < list[3] < list[4]:
    for i in range(n):
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

for i in range(n):
    print(list[i],end=" ")