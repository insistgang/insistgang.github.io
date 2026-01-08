---
title: shell教程（三）基本语句
tags:
  - shell
  - linux
categories:
  - 教程
  - Linux
cover: img/linux.png
abbrlink: 70f4e8c0
date: 2022-01-06 22:53:50
---

引用：

https://www.acwing.com/file_system/file/content/whole/index/content/2855883/

## 判断语句

### if…then形式
类似于C/C++中的if-else语句。

### 单层if

命令格式：

```shell
if condition
then 
	语句1
	语句2
	...
fi
```

示例：

```shell
a=3
b=4

if [ "$a" -lt "$b" ] && [ "$a" -gt 2]
then
	echo ${a}在范围内
fi
```

### 单层if-else

命令格式

```shell
if condition
then
	语句1
	语句2
	...
else
	语句1
	语句2
	...
fi
```

示例：

```shell
a=3
b=4

if ![ "$a" -lt "$b" ]
then
	echo ${a}不小于${b}
else
	echo ${a}小于${b}
fi
```

输出结果：

```shell
3小于4
```

多层if-elif-elif-else

命令格式

```shell
if condition
then
	语句1
	语句2
	...
elif condition
then
	语句1
	语句2
	...
elif condition
then
	语句1
	语句2
	...
else
	语句1
	语句2
	...
fi
```

示例：

```shell
a=4

if [ $a -eq 1]
then
	echo ${a}等于1
elif [ $a -eq 2]
then
	echo ${a}等于2
elif [ $a -eq 3]
then
	echo ${a}等于3
else
	echo 其他
fi
```

输出结果

```
其他
```

### case…esac形式

类似于`c/c++`中的`switch`语句

命令格式

```shell
case $变量名称 in
	值1）
		语句1
		语句2
		...
		;;  # 类似于c/c++中的break
	值2）
		语句1
		语句2
		...
		;;  # 类似于c/c++中的default
esac	
```

示例：

```shell
a=4

case $a in
    1)
        echo ${a}等于1
        ;;  
    2)
        echo ${a}等于2
        ;;  
    3)                                                
        echo ${a}等于3
        ;;  
    *)
        echo 其他
        ;;  
esac
```

输出结果：

```
其他
```

## 循环语句

### for...in...do...done

命令格式：

```shell
for var in val1 val2 val3
do
	语句1
	语句2
	...
done
```

示例1，输出a 2 cc，每一个元素一行：

```shell
for i in a cc
do
	echo $i
done
```

示例2，输出当前路径下的所有文件名，每个文件名一行：

```shell
for file in `ls`
do
	echo $file
done
```

示例3，输出1-10

```shell
for i in $(seq 1 10)
do
	echo $i
done
```

示例4，使用{1..10}或者{a..z}

```shell
for i in {a..z}
do
	echo $i
done
```

### for ((…;…;…)) do…done

命令格式:

```shell
for ((expression;condition;expression))
do
	语句1
	语句2
done
```

示例，输出1-10，每个数占一行：

```shell
for ((i=1;i<=10;i++))
do
	echo $i
done
```

### while...do..done循环

命令格式：

```shell
while condition
do
	语句1
	语句2
	...
done
```

示例，文件结束符为`ctrl+d`，输入文件结束符后`read`指令返回false。

```shell
while read name
do
	echo $name
done
```

### until...do...done循环

当条件为真时结束。

命令格式：

```shell
until condition
do
	语句1
	语句2
	...
done
```

示例，当用户输入`yes`或者`YES`时结束，否则一直等待读入。

```shell
until [ "${word}" == "yes" ] || [ "${word}" == "YES" ]
do
	read -p "Please input yes/YES to stop this program: " word
done
```

### break命令

跳出当前一层循环，注意与`c/c++`不同的是：`break`不能跳出`case`语句。

示例：

```shell
while read name
do
	for((i=1;i<10;i++))
	do
		case $i in
			8)
				break
				;;
			*)
				echo $i
				;;
		esac
	done
```

该示例每读入非EOF的字符串，会输出一遍1-7。

该程序输入`ctrl+d`文件结束符来结束，也可以直接用`ctrl+c`杀掉改进程。

### continue命令

跳出当前循环。

示例：

```shell
for((i=1;i<=10;i++))
do
	if [ `expr $i % 2` -eq 0 ]
	then
		continue
	fi
	echo $i
done
```

该程序输出1-10中的所有奇数。

### 死循环的处理方式

`ctrl+c`

## 函数

`bash`中的函数类似于`C/C++`中的函数，但`return`的返回值与`C/C++`不同，返回的是`exit code`，取值为0-255，0表示正常结束。

如果想获取函数的输出结果，可以通过`echo`输出到`stdout`中，然后通过`$(function_name)`来获取`stdout`中的结果。

函数的`return`值可以通过`$?`来获取。

命令格式：

```shell
[function] func_name() {  # function关键字可以省略
    语句1
    语句2
    ...
}
```

### 不获取 `return`值和`stdout`值

示例

```shell
func() {
    name=yxc
    echo "Hello $name"
}

func
```

输出结果：

```shell
Hello insistgang
```

### 获取`return`值和`stdout`值
不写`return`时，默认`return 0`。

示例

```shell
func() {
    name=insistgang
    echo "Hello $name"
    return 123
}


output=$(func)
ret=$?

echo "output = $output"
echo "return = $ret"

```


输出结果：

```shell
output = Hello insistgang
return = 123
```

### 函数的输入参数
在函数内，`$1`表示第一个输入参数，`$2`表示第二个输入参数，依此类推。

注意：函数内的`$0`仍然是文件名，而不是函数名。

示例：

```shell
echo $(func 10)func() {  # 递归计算 $1 + ($1 - 1) + ($1 - 2) + ... + 0
    word=""
    while [ "${word}" != 'y' ] && [ "${word}" != 'n' ]
    do
        read -p "要进入func($1)函数吗？请输入y/n：" word
    done
    if [ "$word" == 'n' ]
	then
    echo 0
    return 0
	fi  

	if [ $1 -le 0 ] 
	then
    	echo 0
    	return 0
	fi  

	sum=$(func $(expr $1 - 1))
	echo $(expr $sum + $1)
}

echo $(func 10)
```


输出结果：

```
55
```

### 函数内的局部变量
可以在函数内定义局部变量，作用范围仅在当前函数内。

可以在递归函数中定义局部变量。

命令格式：

```shell
local 变量名=变量值
```

例如：

```shell
#! /bin/bash

func() {
    local name=insistgang
    echo $name
}
func

echo $name
```


输出结果：

```shell
insistgang
```

第一行为函数内的name变量，第二行为函数外调用name变量，会发现此时该变量不存在。

## exit命令

`exit`命令用来退出当前`shell`进程，并返回一个退出状态；使用`$?`可以接收这个退出状态。

`exit`命令可以接受一个整数值作为参数，代表退出状态。如果不指定，默认状态值是 0。

`exit`退出状态只能是一个介于 0~255 之间的整数，其中只有 0 表示成功，其它值都表示失败。

示例：

创建脚本`test.sh`，内容如下：

```shell
#! /bin/bash

if [ $# -ne 1 ]  # 如果传入参数个数等于1，则正常退出；否则非正常退出。
then
    echo "arguments not valid"
    exit 1
else
    echo "arguments valid"
    exit 0
fi
```

执行该脚本：

```shell
chmod +x test.sh
./test.sh acwing
arguments valid
echo $?  # 传入一个参数，则正常退出，exit code为0
0
./test.sh 
arguments not valid
echo $?  # 传入参数个数不是1，则非正常退出，exit code为1
1
```

每个进程默认打开3个文件描述符：

- `stdin`标准输入，从命令行读取数据，文件描述符为0
- `stdout`标准输出，向命令行输出数据，文件描述符为1
- `stderr`标准错误输出，向命令行输出数据，文件描述符为2

可以用文件重定向将这三个文件重定向到其他文件中。

### 重定向命令列表

| 命令               | 说明                                      |
| ------------------ | ----------------------------------------- |
| `command > file`   | 将`stdout`重定向到`file`中                |
| `command < file`   | 将`stdin`重定向到`file`中                 |
| `command >> file`  | 将`stdout`以追加方式重定向到`file`中      |
| `command n<< file` | 将文件描述符`n`重定向到`file`中           |
| `command n>> file` | 将文件描述符`n`以追加方式重定向到`file`中 |

### 输入和输出重定向

创建bash.sh脚本：

```shell
#! /bin/bash

read a
read b

echo $(expr "$a" + "$b")
```

创建input.txt，里面的内容为：

```
3
4
```

执行命令：

```shell
chmod +x test.sh  # 添加可执行权限
./test.sh < input.txt > output.txt  # 从input.txt中读取内容，将输出写入output.txt中
cat output.txt  # 查看output.txt中的内容
7
```

## 引入外部脚本

类似于`C/C++`中的`include`操作，`bash`也可以引入其他文件中的代码。

语法格式：

```shell
. filename  # 注意点和文件名之间有一个空格

或

source filename
```

### 示例

创建`test1.sh`，内容为：

```shell
#! /bin/bash

name=insistgang  # 定义变量name
```

然后创建`test2.sh`，内容为：

```shell
#! /bin/bash

source test1.sh # 或 . test1.sh

echo My name is: $name  # 可以使用test1.sh中的变量
```


执行命令：

```shell
chmod +x test2.sh 
./test2.sh 
My name is: insistgang
```