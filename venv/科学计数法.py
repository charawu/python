print("请输入科学计数法数")
num = str(input())

if "e" in num or "E" in num:
    if num.find("e") > 0:
        head = num[:num.find("e")]
        tail = num[num.find("e") + 1:]
    elif num.find("E") > 0:
        head = num[:num.find("E")]
        tail = num[num.find("E") + 1:]
    
    sum = float(head) * 10.0 ** float(tail)
    print(sum)

else:
    print("输入有误")


#by .v