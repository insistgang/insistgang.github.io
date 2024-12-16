---
title: 《青少年Python编程入门》案例(一)
tags:
  - case
  - python
categories:
  - 读书笔记
  - Python
cover: img/studypython.png
abbrlink: ae2ba9b2
date: 2022-02-10 19:37:26
---

## 第一章案例

### CH0101.py

```python
print('Python is great fun!')
```

### CH0102.py——第一个Python程序

```python
# 第一个Python程序
"""内置函数(BIF)
input()取得输入值
print()函数在屏幕上输入字符串 """
name=input('请输入你的名字：')
print('hello!'+name)
```

请输入你的名字：123

hello!123

### CH0103.py——时间显示

```python
import time # 导入时间模块
name = input('你的名字->')
print('Hi',name,'现在时间：')
print()# 输出空白行
print(time.ctime())
```

你的名字->liugang

Hi liugang 现在时间：



Thu Feb 10 17:42:25 2022



### 作业 

一、利用print()函数输出下列运算的结果

(1) 78+56

(2) 125-41

```python
print(78+56) #134
print(125-41) #84
```

二、参考CH0103.py，输出"Hello! 自己的名字"。

```python
name = input('你的名字->')
print('Hello!',name)
```



三、输入如下小图案

 \----- 

/Hello\

|Mary!|

\      /

 \----- 

\>>> |

```python
print(" ----- \n/Hello\\\n|Mary!|\n\\      /\n ----- \n>>> |")
```

## 第二章案例

### CH0201.py——用eval()函数取得输入值

```python
num1,num2,num3=eval(
input('请输入三个数值，以逗号隔开'))
total=num1+num2+num3
print('数值合计：',total)
```

请输入三个数值，以逗号隔开1,2,3

数值合计： 6

### CH0202.py——用内置函数转换为十进制数值

```python
number=int(input('输入一个数值->'))
print('类型：',type(number))
print('二进制：',bin(number))
print('八进制：',oct(number))
print('十六进制：',hex(number))
print('十进制：',number)
# 使用format函数删除前缀字符
print('二进制：',format(number,'b'))
print('八进制：',format(number,'o'))
print('十六进制:',format(number,'x'))
```

输入一个数值->15

类型： <class 'int'>

二进制： 0b1111

八进制： 0o17

十六进制： 0xf

十进制： 15

二进制： 1111

八进制： 17

十六进制: f



### CH0203.py——认识正、负无穷数

```python
import math # 导入模块
a=1E309
print('a=1E309,输出',a)
# 输出True，表示它是NaN
print('为NaN?',math.isnan(float(a/a)))
b=-1E309
print('b=-1E309，输出',b)
# 输出True，表示它是Inf
print('为Inf?',math.isinf(float(-1E309)))
```

a=1E309,输出 inf

为NaN? True

b=-1E309，输出 -inf

为Inf? True

正无穷：Inf  负无穷：Neg 非数字 NaN

### CH0204.py——基本的加减乘除操作

```python
num1=3+5j;num2=2-4j;
result=num1+num2
print(result)# 输出5+1j
result=num1-num2
print(result)# 输出1+9j
result=num1*num2
print(result)# 输出26-2j
result=num1/num2
print(result)# 输出-0.7+1.1j
```

(5+1j)

(1+9j)

(26-2j)

(-0.7+1.1j)



### CH0205.py——Decimal类型的使用

```python
from decimal import Decimal
num1=Decimal('0.5534')
num2=Decimal('0.427')
num3=Decimal('0.37')
print('相加',num1+num2+num3)#1.3504
print('相减',num1-num2-num3)#-0.2436
print('相乘',num1*num2*num3)#0.087431666
print('相除',num1/num2)#1.296018735362997658079625293
```

相加 1.3504

相减 -0.2436

相乘 0.087431666

相除 1.296018735362997658079625293



### CH0206.py——将代数转化为表达式

```python
x=23;y=7;# 指定变量x,y的值
z=9*(12/x+(x-5)/(y+9))
print('z=',z)
```

z= 14.820652173913045

### CH0207.py——使用math模块

```python
import math
num1,num2=eval(
input('输入两个数值取得余数->'))
#求平方根
print(num1,'平方根：',num1**0.5)
print(num2,'平方根：',num2**0.5)
print('数值',num1,'的3次方:',math.pow(num1,3))
print('数值',num2,'的立方根:',math.pow(num2,1.0/3))
#GCD为最大公约数
print('余数：',math.fmod(num1,num2))
print('GCD:',math.gcd(num1,num2))
print('两数平方后再开根号',math.hypot(num1,num2))
# 自然对数
print('指数函数：',math.e)
print('方法exp(4)=',math.exp(4))
```

输入两个数值取得余数->69,5

69 平方根： 8.306623862918075

5 平方根： 2.23606797749979

数值 69 的3次方: 328509.0

数值 5 的立方根: 1.7099759466766968

余数： 4.0

GCD: 1

两数平方后再开根号 69.18092222571191

指数函数： 2.718281828459045

方法exp(4)= 54.598150033144236



### 自我评价

**填空题**

一、Python中的所有数据都是以对象形式表达，每个对象都具有**身份、类型、值**

二、请简单说明下列变量定义发生了什么问题？

```python
raise=78# 1
7seven=258# 2
brith='1988/5/25'
print(BIRTH)# 3
```

1 raise是保留字 不能当做变量

2 7seven 变量命名不能以数字开头

3 Python程序的大小写不兼容

三、将十进制数值以bin()函数转化成二进制，oct()函数转化成八进制，hex()函数转换成十六进制。

四、下列语句说明了什么？

```python
number=125
number='457'
```

number从数据类型125变成了字符类型457

五、下列语句会输出什么？

```python
number,grade=78,65
number,grade=grade,number
print(number,grade)
```

输出 65 78

两个变量进行了交换操作。

六、bool类型有两个值：以数值"1"表示True；数值"0"表示False。

七、复数由实部和虚部组成，可以由内置函数complex()进行类型的转换。

八、下列语句的输出值是多少？

```python
from fractions import Fraction
number=Fraction(256,788)
print(number)
```

64/197

九、下述表达式的运算结果：

```python
348/25
348//25
358%25
81**0.3
```

13.92

13 

8

3.7371928188465517

十、将代数表达式(x^2+y^2)/3转化为Python表达式：

```python
print((x**2+y**2)/3)
```

十一、下列函数和方法经过运算后的结果：

```python
import math
math.pow(64,7) # 4398046511104.0
pow(64,7,37) # 27
```

十二、下列语句经过比较、逻辑运算会输出什么值？

```python
a,b=125,67
a<b# False
a!=b# True
not a<b#True
(a%5==0)or(b%11==0) #True
```

**实践题**

一、王小明的考试成绩如下：语文78分、数学63分，英语92分。如何用eval()函数来输入这三科的分数，并计算它们的总分和平均值。

```python
num1,num2,num3=eval(input('输入三科成绩用逗号隔开:'))
sum=num1+num2+num3
print('总分',sum)
print('平均分',sum/3)
```

二、王小明打算买100支铅笔在学校使用，他询问后发现最便宜的铅笔是每支4.35元，请问，他至少要花多少钱？要如何编写程序？会发生什么问题？

```python
至少要花435元
print(4.35*100)
434.99999999999994
精度出现问题
```

三、已知x=78,y=126,利用math模块求根号x^2+y^2及x和y的最大公约数

```python
import math
x=78;y=126
num=x*x+y*y
print(num**0.5)
print(x,y,'最大公约数是',math.gcd(x,y))
```

148.18906842274163

78 126 最大公约数是 6