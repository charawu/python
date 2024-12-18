#题目:兔子数列
#姓名:武洪斌
#参考https://baike.sogou.com/v267267.htm?fromTitle=%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97

#分析，兔子在第一个月时，无法繁殖，一个月后长为大兔子，再过一个月后开始繁殖，所以当第二个月后兔子才开始繁殖

list1=[]
for i in range(12):
    if i < 2:
        list1.append(1)
    else:
        list1.append(list1[i - 1] + list1[i - 2])


print(list1[11])