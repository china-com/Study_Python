# 整数类型-->int
# python3里，不管数字有多大，该数字都是int类型
# Python2里，则不同，数字的长度超过int的表示范围后，将会是long类型
'''
# int()   将数字字符串转化成数字
a="123"
# a此时为字符串
print(type(a),a)
# <class 'str'> 123
b=int(a)
print(type(b),b)
# <class 'int'> 123

num="a"
v=int(num,base=16)
# 将num以十六进制转换成十进制
print(v)
# 10
'''

# 当前数字的二进制，至少需要N来表示
# a=1 #1
# b=4 #100
# c=10    #1010
# print(a.bit_length()) #1
# print(b.bit_length()) #2
# print(c.bit_length()) #4

# 字符串
# 首字母大写
# test="sayschj"
# print(test.capitalize()) #Sayschj
# # 所有字母小写，casefold更强大，除引文外其他语言中也会存在很多大小写的对应关系，lower()只对英文字母有效
# print(test.casefold())
# print(test.lower())
# # sayschj

# 设置宽度，并将内容居中
# 20代指总长度
# * 空白位置填充，只能是一个字符（字母，数字，中文等），可选参数，默认用空格填充
test="Sayschj"
# print(test.center(20,"*"))
# ******Sayschj*******

# # 去字符串中寻找，某个子序列出现的次数,区分大小写,后两位参数分别表示其实位置和终止位置
# print(test.count("s"))
# # 1
#
# print(test.count('ch',3,6))
# # 1

# 以什么什么开始
# 以什么什么结尾,后面也可跟上两个参数，起始位置和终止位置
# print(test.endswith('hj'))
# print(test.startswith('h'))
# True
# False

# 从开头往后找，找到第一个后，获取其出现的第一个位置
# def find(self, sub, start=None, end=None)
# print(test.find("ay",0,6))

# format格式化,将字符串中的展位符替换未指定的值
# test='i am {0},age {1}'
# print(test)
# i am {0},age {1}
# v=test.format('sayschj',18)
# print(v)
# i am sayschj,age 18

# FormatStr='I am {name},age {a}'
# print(FormatStr)
# I am {name},age {a}
# FormatString=FormatStr.format(name='Sayschj',a=18)
# print(FormatString)
# I am Sayschj,age 18
test='abcdegfhsdfhksjs'
print(test.expandtabs(8))