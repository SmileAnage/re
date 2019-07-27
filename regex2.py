"""
match　对象属性演示
"""
import re

pattern = r'(ab)cd(?P<pig>ef)'
regex = re.compile(pattern)
obj = regex.search('abcdefghi', 0, 8)  # match对象

# 属性变量
print(obj.pos)  # 目标字符串开始位置
print(obj.endpos)  # 目标字符串结束位置
print(obj.re)  # 正则表达式
print(obj.string)  # 目标字符串
print(obj.lastgroup)  # 最后一组组名
print(obj.lastindex)  # 最后一组序列号

# 属性方法
print(obj.span())  # 匹配内容在字符串中位置
print(obj.start())  # 匹配内容在字符串起始位置
print(obj.end())  # 匹配内容在字符串结束位置
print(obj.groupdict())  # 破获组字典
print(obj.group())  # 子组对应内容元组
print(obj.groups())  # 获取match对应内容
print(obj.group('pig'))