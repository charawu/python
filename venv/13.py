#题目:鸡兔同笼
#姓名:武洪斌
#有若干只鸡兔同在一个笼子里，从上面数，有35个头，从下面数，有94只脚。问笼中各有多少只鸡和兔？(题目参考：https://baike.baidu.com/item/%E9%B8%A1%E5%85%94%E5%90%8C%E7%AC%BC/5907332)

for i in range(35):
    for j in range(35):
        if  2*i + 4*j == 94 and i + j == 35:
            print(i,j)