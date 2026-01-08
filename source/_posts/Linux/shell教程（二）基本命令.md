---
title: shell教程（二）基本命令
tags:
  - shell
  - linux
categories:
  - 教程
  - Linux
cover: img/linux.png
abbrlink: e1e84ee1
date: 2022-01-05 20:43:54
---

引用：

https://www.acwing.com/file_system/file/content/whole/index/content/2855883/

## expr命令

`expr`命令用于求表达式的值，格式为：

```shell
expr 表达式
```

表达式说明：

- 用空格隔开每一项
- 用反斜杠放在shell特定的字符前面(发现表达式运行错误时，可以试试转义)
- 对包含空格和其他特殊字符的字符串要用引号括起来
- expr会在`stdout`中输出结果。如果为逻辑关系表达式，则结果为真，`stdout`为1，否则为0。
- expr的`exit code`：如果为逻辑关系表达式，结果为真，`exit code`为0，否则为1。

### 字符串表达式

- `length STRING`返回`STRING`的长度
- `index STRING CHARSET` `CHARSET中`任意单个字符在`STRING`中最前面的字符位置，**下标从1开始**。如果在`STRING`中完全不存在`CHARSET中`的字符，则返回0。
- `substr STRING POSITION LENGTH` 返回`STRING`字符串中从`POSITION`开始，长度最大为`LENGTH`的字符串。如果`POSITION`或`LENGTH`为负数，0或非数值，则返回空字符串。

示例：

```shell
str="Hello World!"

echo `expr length "$str"`  # ``不是单引号，表示执行该命令，输出12
echo `expr index "$str" aWd`  # 输出7，下标从1开始
echo `expr substr "$str" 2 3`  # 输出 ell

```

### 整数表达式

`expr`支持普通的算术操作，算术表达式优先级低于字符串表达式，高于逻辑关系表达式。

- `+ -`

  加减运算。两端参数会转换为整数，如果转换失败，则报错。

- `* / %`

  乘，除，取模运算。两端参数会转换为整数，如果转换失败则报错。

- `()`可以该表优先级，但需要用反斜杠转义

示例：

```shell
a=3
b=4

echo `expr $a + $b`  # 输出7
echo `expr $a - $b`  # 输出-1
echo `expr $a \* $b`  # 输出12，*需要转义
echo `expr $a / $b`  # 输出0，整除
echo `expr $a % $b` # 输出3
echo `expr \( $a + 1 \) \* \( $b + 1 \)`  # 输出20，值为(a + 1) * (b + 1)
```

### 逻辑关系表达式

- `|`

  如果第一个参数非空且非0，则返回第一个参数的值，否则返回第二个参数的值，但要求第二个参数的值也是非空或0，否则返回0。如果第一个参数是非空或0时，不会计算第二个参数。

- `&`

  如果两个参数都非空且非0，则返回第一个参数，否则返回0。如果第一个参为0或为空，则不会计算第二个参数。

- `< <= = == != >= >`

  比较两端的参数，如果为true，则返回1，否则返回0。"=="是"="的同义词。"expr"首先尝试将两端参数转换为整数，并做算术比较，如果转换失败，则按字符集排序规则做字符比较。

- `()`可以该表优先级，但需要用反斜杠转义

示例：

```shell
a=3
b=4

echo `expr $a \> $b`  # 输出0，>需要转义
echo `expr $a '<' $b`  # 输出1，也可以将特殊字符用引号引起来
echo `expr $a '>=' $b`  # 输出0
echo `expr $a \<\= $b`  # 输出1

c=0
d=5

echo `expr $c \& $d`  # 输出0
echo `expr $a \& $b`  # 输出3
echo `expr $c \| $d`  # 输出5
echo `expr $a \| $b`  # 输出3
```

## read命令

`read`命令用于从标准输入中读取单行数据。当读到文件结束符时，`exit code`为1，否则为0。

参数说明

- `-p`：后面可以接提示信息
- `-t`：后面跟秒数，定义输入字符的等待时间，超过等待时间后会自动忽略此命令

```shell
read name  # 读入name的值
liugang
echo $name
liugang
read -p "请输入你的名字:" -t 30 name
请输入你的名字: liugang
echo $name
liugang
```

## printf命令

`printf`命令用于格式化输出，类似于`c/c++`中的`printf`函数。

默认**不会在字符串末尾添加换行符。**

命令格式：

```shell
printf format-string[arguments...]
```

**用法示例**

脚本内容：

```shell
printf "%10d.\n" 123  # 占10位，右对齐
printf "%-10.2f.\n" 123.123321  # 占10位，保留2位小数，左对齐
printf "My name is %s\n" "yxc"  # 格式化输出字符串
printf "%d * %d = %d\n"  2 3 `expr 2 \* 3` # 表达式的值作为参数
```

输出结果：

```shell
       123.
123.12    .
My name is yxc
2 * 3 = 6
```

## test命令与判断符号[]

### 逻辑运算符&&和||

- `&&`表示与，`||`表示或

- 二者具有短路原则：

  `expr1 && expr2`：当`expr1`为假时，直接忽略`expr2`

  `expr1 || expr2`：当`expr1`为真时，直接忽略`expr2`

- 表达式的`exit code`为0，表示真；为非零，表示假。(与`c/c++`中定义完全相反)

### test命令

在命令行中输入`man test`，可以查看`test`命令的用法。

`test`命令用于判断文件类型，以及变量做比较。

`test`命令用`exit code`返回结果，而不是用`stdout`。0表示真，非0表示假。

列如：

```shell
test 2 -lt 3  # 为真，返回值为0
echo $?  # 输出上个命令的返回值，输出0
```

```shell
ls #列出当前目录下的所有文件
output.txt test.sh tmp
test -e test.sh && echo "exist" || echo "Not exist"
exist  # test.sh存在
test -e test2.sh && echo "exist" || echo "Not exist"
Not exist # test.sh不存在
```

### 文件类型判断

命令格式：

```shell
test -e filename   # 判断文件是否存在
```

| 测试参数 | 代表意义     |
| -------- | ------------ |
| -e       | 文件是否存在 |
| -f       | 是否为文件   |
| -d       | 是否为目录   |

### 文件权限判断
命令格式：

```shell
test -r filename  # 判断文件是否可读
```

| 测试参数 | 代表意义       |
| -------- | -------------- |
| -r       | 文件是否可读   |
| -w       | 文件是否可写   |
| -x       | 文件是否可执行 |
| -s       | 是否为非空文件 |
### 整数间的比较
命令格式：

```shell
test $a -eq $b  # a是否等于b
```

| 测试参数 | 代表意义       |
| -------- | -------------- |
| -eq      | a是否等于b     |
| -ne      | a是否不等于b   |
| -gt      | a是否小于b     |
| -lt      | a是否大于b     |
| -ge      | a是否大于等于b |
| -le      | a是否小于等于b |

### 字符串比较

| 测试参数          | 代表意义                                               |
| ----------------- | ------------------------------------------------------ |
| test -z STRING    | 判断STRING是否为空，如果为空，则返回true               |
| test -n STRING    | 判断STRING是否非空，如果非空，则返回true（-n可以省略） |
| test str1 == str2 | 判断str1是否等于str2                                   |
| test str1 != str2 | 判断str1是否不等于str2                                 |



### 多重条件判定

命令格式：

```shell
test -r filename -a -x filename
```

| 测试参数 | 代表意义                                          |
| -------- | ------------------------------------------------- |
| -a       | 两个条件是否同时成立                              |
| -o       | 两个条件是否至少一个成立                          |
| !        | 取反。如test ! -x file,当file不可执行时，返回true |

### 判断符号[]

[]与test用法几乎一模一样，更常用于if语句中。另外[[]]是[]的加强版，支持的特性更多。

例如：

```shell
[ 2 -lt 3 ]  # 为真，返回值为0
echo $?  # 输出上个命令的返回值，输出0
```

```shell
ls
homework output.txt test.sh tmp
[ -e test.sh ] && echo "exist" || echo "not exist"
exist # test.sh 文件存在
[ -e test2.sh ] && echo "exist" || echo "not exist"
not exist # test2.sh 文件不存在
```

注意：

- `[]`内的每一项都要用空格隔开
- 中括号内的变量，最好用双引号括起来
- 中括号内的常数，最好用单或双引号括起来

例如：

```shell
name="acwing yxc"
[ $name == "acwing yxc" ]  # 错误，等价于 [ acwing yxc == "acwing yxc" ]，参数太多
[ "$name" == "acwing yxc" ]  # 正确
```

