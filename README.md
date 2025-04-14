# python基础教程 {#main-title}
[toc]

## 1.python基础语法

### 1.1缩进

这是一个基础的判断语句
```python
a = 1
b = 2
if b > a:
    print(a,b)
```
此处的缩进指的就是print前的四个空格

```python
a = 1
b = 2
if b > a:
print(a,b)
```
此处就是没有缩进的情况,会直接报错
一般情况下在代码编辑器中回车会自动缩进

<span style="color:red;">此处是缩进用途原理展示
```python
a = "b"
for i in range(3):
    print(i)

print(a)
```
以上代码运行结果为
```python
0
1
2
b
```
因为第一个print缩进了,所以它的运行是在<span style="color:#ff00ff">for</span>循环内的,所以会遍历到3
而第二个print是在没有缩进,所以是与<span style="color:#ff00ff">for</span>并列的,要在<span style="color:#ff00ff">for</span>运行完毕后才运行

<span style="color:red">总结:有缩进的代码是包含在它上一个缩进代码内的

### 1.2注释

因为注释过于简单此处就随便讲一下

一下是两种注释方法
```python
print("a")  #此处中文是注释(也就是在"#"后的所有)

#print("b")  #此处代码和中文字符都一起被注释了

"""
print("c")
#此处是多行注释
#一下代码和中文字符均被注释(也就是被"""包起来的所有)
"""
```
以上代码运行结果为
```python
a
```
因为只有print("a")没有被注释

### 1.3基本输入与输出
输入函数为input()
输出函数为print()
```python
a = input("请输入a的值:")
print(a)
```
以下为运行结果
```python
请输入a的值:2
2
```
input中被""引起来的内容和使用print一样有输出作用
print函数()内有许多参数,此处不赘述要了解请参阅</https://www.cnblogs.com/yanpeng1535/p/18529828>

### 1.4变量
以下为python的变量命名规则
```markdown
在Python中，变量命名规则非常重要，因为它们不仅决定了变量的可读性和可维护性，还涉及到Python的语法解析。以下是Python中变量命名的基本规则：
    1.变量名只能包含字母、数字或下划线：变量名不能包含空格、连字符（-）、感叹号(!)等特殊字符。
    2.变量名不能以数字开头：例如，1_name 是无效的，而 name1 是有效的。
    3.变量名是大小写敏感的：这意味着 variable 和 Variable 被视为两个不同的变量。
    4.变量名可以包含下划线：虽然下划线不是必须的，但使用下划线可以增强变量的可读性。例如，使用 my_variable 而不是 myvariable。
    5.避免使用Python关键字：Python有一些预定义的关键词（如 if、for、while 等），这些关键词不能用作变量名。
    6.遵循PEP 8风格指南：虽然不是强制性的，但遵循PEP 8 -- Style Guide for Python Code中的命名约定是一个好习惯。例如，对于函数名和变量名，通常使用小写字母和下划线（snake_case）作为命名方式。
    7.描述性命名：选择描述性的变量名，使代码更易于理解。例如，使用 user_name 而不是 un。
    8.避免使用Python内置函数或模块的名字：虽然这不是一个严格的规则，为了避免混淆和潜在的错误，最好避免使用如 list、str、len 等作为变量名。
```
例子就不举例了,记住就行

#### 1.4.1赋值
关于变量的赋值就简单讲解
定义变量并赋值
```python
a = 10
```
这就是一个最简单的定义变量a并给a赋值为10
也可以同时定义多个并一起赋值
```python
a,b,c = 10,20,30
```

## 2数据类型
python数据类型分为数字和组,我们先讲数字组之后再说
### 2.1数字类型
在python中数字类型有整型<span style="color:red">int</span>,浮点型<span style="color:red">float</span>,布尔型<span style="color:red">bool</span>,复数<span style="color:red">complex</span>
说人话,就是整数,小数,真和假,至于复数我也是才知道的,和数学中的复数一个概念
浮点数有取值范围需要注意,范围为<span style="color:red">-10^308^~10^308^
此外还有一个分数类型,以下是示例
```python
#分数类型要使用Fraction模块
from fractions import Fraction
a = Fraction(1,4)
print(a)
```
运行结果为
```python
1/4
```
### 2.2数字运算
以下为python中的运算符
```python
**  幂运算
~   按位取反
-   负号也表示减法
*   乘法
%   取余
/   除法
//  除法但返回值取整
+   加法
<<  左移位
>>  右移位
&   按位与
^   按位异或
|   按位或
<   小于
>   大于
>=  大于等于
<=  小于等于
==  相等
!=  不等于
not 逻辑非
and 逻辑与
or  逻辑或
```
#### 2.2.1运算优先级
python中运算优先级与数学上一致,如有不清楚请复习小学数学

### 2.3字符串类型str
直接说人话就是使用'a',"b",'''c''',"""d"""括起来的就是字符串
三引号字符串也可以跨换
此外三引号和三双引号也被用于注释,以下会做出解释
```python
a = '''这是一段字符'''
print(a)

print("--------------")
b = ''' 这是
一段
字符
'''
print(b)

'''
这是一段注释
'''
```
运行结果为:
```python
这是一段字符
--------------
 这是
一段
字符
```
这就是两者的区别
### 2.4转义字符
转义字符用于表示不能直接表示的字符
```python
\\  反斜线
\'  单引号
\"  双引号
\a  响铃符
\b  退格符
\f  换页符
\n  换行符
\r  回车符
\t  制表符
\v  垂直制表符
\0  NULL空字符
```

### 2.5字符串操作
直接用示例了,不过多讲解
1.
```python
#  in判断字符串包含关系
#  in的返回值为bool布尔值
x = "abcd"
print("a" in x)
```
运行结果为:
```python
True
```
2.

```python
#  +表示合并字符串
x = "abc"
v = "def"
print(x + v)
```
运行结果为:
```python
abcdef
```
3.
```python
#  *用于复制字符串
x = "ab"
print(x * 3)
```
运行结果为:
```python
ababab
```

### 2.6字符串索引和切片
第40页
