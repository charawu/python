#题目:有两个集合集合a和集合B计算两个集合的差集,并集和交集.从键盘输入一个数并判断在a集合还是在b集合
#姓名:武洪斌

A = {1,2,3,4,5}
B = {4,5,6,7,8}

print("集合A为:",A)
print("集合B为:",B)
print()
print("A与B的差集为:",A-B)
print("A与B的并集为:",A | B)
print("A与B的交集为:",A & B)

print("请输入一个数以此判断在那个集合")
num = int(input())
if num in A:
    print(num,"在集合A中")
if num in B:
    print(num,"在集合B中")