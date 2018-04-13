#Python变量、条件语句、基本数据类型：
# 第一行代码：
print("HelloWorld!")

# 假如文件名是：1.
# py
# python 1.py
# 在Linux系统下，如果想通过：./ 1.py来执行代码
# 则需要在python文件的内部在上：
# !/usr/bin/env python	//python解释器的路径
#  具体代码

# 文件编码：
# -*- coding:utf8 -*-
# 使用python3时无需关注
# 使用python2时，每个文件中只要出现中文，头部就的加文件的编码注释

# 代码块：
# if 条件：
# // 代码块内容，注意缩进
# else 条件:
# // 代码块内容，注意缩进

# 在条件语句中，对于某个满足要求的判断语句，不想输出任何内容，则在内部代码块中输入：pass
if 1 == 1:
    pass
else:
    print("sb")

# 字符串（引号）：
# name = "helloworld!"
# name = 'syayschj'
# name = """你好，世界"""
# name = '''哈哈'''
# 这些都是字符串。

# 字符串加法：略
#
# 字符串乘法：
n1 = "sayschj"
n2 = n1 * 10
print(n2)  #sayschjsayschjsayschjsayschjsayschjsayschjsayschjsayschjsayschjsayschj
# 字符串重复出现的次数
'''
数字：
age = 18
a1 = 4 * 4
a2 = 4 ** 4 # 表示4的4次方
a2 = 39 / 8 # // 4.875，余数
a3 = 39 % 8 # 7，获取39除以8得到的余数
a2 = 39 // 8  #4，商
'''

a1 = 13
temp = a1 / 2
if temp == 0:
    print("偶数")
else:
    print("奇数")
'''
input的用法：
永远等待，知道用户输入了值，就将输入的值赋值给一个变量，在键盘上无论输入什么，都将以字符串的形式存在

in =input('请输入：')
>> 10
in ="10"
将字符串装换成数字： new_in = int(in)

死循环：
while 1 == 1:
    print("ok") // 将一直执行打印操作
'''
'''
用户登录（三次机会重试）：
count = 0
while count < 3:
    user = input(">>>")
    pwd = input(">>>")
    if user=="sayschj" and pwd=="123456"：
    print("欢迎登录！")
    print("...........")
    break
else:
    print("用户名或密码错误！")
    count = count + 1
'''

name = "abc defg"
print(name.title())  # Abc Defg	以首字母大写显示每个单词
print(name.upper())  # 转大写
print(name.lower())  # 转小写

'''
str = "   python   "
str.rstrip()  # 清除字符串后面出现的空格 "   python"
str.lstrip()  # 清除字符串前面出现的空格 "python   "
str.strip()  # 清除字符串两端的空格
'''
age = 18
print("Happy " + str(age) + "rd Brithday!")
# 在字符串中使用数字类型的变量时，需要显式地将数字转换成字符串（使用：str()）,
# 因为，此时Python分不清这个变量到底表示是整数：18, 还是字符表示：1和8.

# 成员运算符in和not in的使用:
# 判断某个东西是否包含在某个字符串的里面
name = "张国荣"
# "张国荣"		字符串
# "张"	字符
# "国荣"	子字符串，子序列
# b = "正"  # Error
# b = "张国"  # OK
b = "张荣"  # Error
if "b" in name:
    print('OK')
else:
    print('Error')

'''
count =1
count +=1
count *=1
count **=1  幂次方
'''