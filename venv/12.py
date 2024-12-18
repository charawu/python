#题目:输出50以内勾股数
#姓名:武洪斌

for i in range(1,50):
    for j in range(1,50):
        for v in range(1,50):
            if i*i + j*j == v*v:
                print(i,j,v)