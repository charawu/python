#题目:判断一年是否为闰年
#姓名:武洪斌

print("请输入年份")
year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print(year,"年是闰年")

elif year % 400 == 0:
     print(year, "年是闰年")
elif (year % 3200 == 0 and year % 172800 == 0):
        print(year, "年是闰年")

#此题闰年判断方法来自https://zhidao.baidu.com/question/2015507156348243508.html