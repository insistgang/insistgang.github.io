---
title: Linux常用文件管理命令
tags: linux
categories:
  - 教程
  - Linux
cover: img/linux.png
swiper_index: 2
swiper_desc: 快速学会使用Linux常用命令
swiper_cover: /img/linux.png
abbrlink: 7e2c5aa3
date: 2022-01-01 19:31:39
---

引用：

https://www.acwing.com/file_system/file/content/whole/index/content/2855530/

## 常用命令介绍

(1) ctrl c: 取消命令，并且换行
(2) ctrl u: 清空本行命令
(3) tab键：可以补全命令和文件名，如果补全不了快速按两下tab键，可以显示备选选项
(4) ls: 列出当前目录下所有文件，蓝色的是文件夹，白色的是普通文件，绿色的是可执行文件
(5) pwd: 显示当前路径
(6) cd XXX: 进入XXX目录下, cd .. 返回上层目录
(7) cp XXX YYY: 将XXX文件复制成YYY，XXX和YYY可以是一个路径，比如../dir_c/a.txt，表示上层目录下的dir_c文件夹下的文件a.txt
(8) mkdir XXX: 创建目录XXX
(9) rm XXX: 删除普通文件;  rm XXX -r: 删除文件夹
(10) mv XXX YYY: 将XXX文件移动到YYY，和cp命令一样，XXX和YYY可以是一个路径；重命名也是用这个命令
(11) touch XXX: 创建一个文件
(12) cat XXX: 展示文件XXX中的内容
(13) 复制文本
    windows/Linux下：Ctrl + insert，Mac下：command + c
(14) 粘贴文本
    windows/Linux下：Shift + insert，Mac下：command + v

## 测试
(0)分别创建文件夹dir_a, dir_b, dir_c
```shell
	mkdir dir_a, dir_b, dir_c
```
(1)将a.txt, b.txt, c.txt 分别复制成: a.txt.bak, b.txt.bak, c.txt.bak
```shell
cp a.txt a.txt.bak
cp b.txt b.txt.bak
cp c.txt c.txt.bak
```
(2)将a.txt, b.txt, c.txt 分别重命名为: a_new.txt, b_new.txt, c_new.txt
```shell
mv a.txt a_new.txt
mv b.txt b_new.txt
mv c.txt c_new.txt
```
(3)将dir_a文件夹下的a.txt, b.txt, c.txt分别移动到文件夹dir_b下
```shell
mv dir_a/* dir_b/
```
(4)将普通文件a.txt, b.txt, c.txt删除
```shell
rm a.txt b.txt c.txt
```
(5)将文件夹dir_a, dir_b, dir_c删除
```shell
rm dir_a dir_b dir_c -r
```
(6)查看task.txt的内容，并按其指示进行操作
```shell
cat task.txt
将task.txt重命名为done.txt, 创建目录dir_a，将done.txt移动到目录dir_a下
mv task.txt done.txt
mkdir dir_a
mv done.txt dir_a/

或者

mkdir dir_a
mv task.txt dir_a/done.txt

```
(7)创建文件夹dir_0, dir_1, dir_2，
将a.txt, b.txt, c.txt复制到dir_0下，重命名为a0.txt, b0.txt, c0.txt;
将a.txt, b.txt, c.txt复制到dir_1下，重命名为a1.txt, b1.txt, c1.txt;
将a.txt, b.txt, c.txt复制到dir_2下，重命名为a2.txt, b2.txt, c2.txt;
```shell
mkdir dir_0 dir_1 dir_2
cp a.txt dir_0/a0.txt
cp b.txt dir_0/b0.txt
cp c.txt dir_0/c0.txt
cp a.txt dir_1/a1.txt
cp b.txt dir_1/b1.txt
cp c.txt dir_1/c1.txt
cp a.txt dir_2/a2.txt
cp b.txt dir_2/b2.txt
cp c.txt dir_2/c2.txt

```
(8)分别在dir_a, dir_b, dir_c文件夹下查看task.txt的内容，并分别按照指示进行操作
```shell
cd dir_a
cat task.txt
将a.txt删除
rm a.txt

cd dir_b
cat task.txt
将b.txt重命名为b_new.txt
mv b.txt b_new.txt

cd dir_c
cat task.txt
c.txt复制成c.txt.bak
cp c.txt c.txt.bak

```
(9)将其中所有txt类型的文件删除
```shell
rm *.txt
```

