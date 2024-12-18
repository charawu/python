#题目:使用for解决百鸡问题(鸡翁一，值钱伍；鸡母一，值钱三；鸡鶵三，值钱一。凡百钱买鸡百只，问鸡翁、母、鶵各几何？)
#姓名:武洪斌

max_x = int(100 / 5)
max_y = int(100 / 3)

for x in range(max_x):
    for y in range(max_y):
        z = 100-x-y
        if 5*x + 3*y + z/3 == 100:
            print(z,y,z)