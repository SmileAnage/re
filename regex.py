"""
regex re模块　　功能函数演示
"""
import re

# 目标字符串
s = 'SmileAnage:1996,BitterCoffee:2000'
pattern = r'\w+:\d+'  # 正则表达式
pattern_0 = r'(\w+):(\d+)'  # 正则表达式

# re模块直接调用findall
l = re.findall(pattern, s)
print(l)

# 显示子组内容
l_0 = re.findall(pattern_0, s)
print(l_0)

# compile对象调用findall
regex = re.compile(pattern)
l = regex.findall(s, 0, 34)
print(l)

# 按照正则表达式切割字符串
l = re.split(r'[:,]', s)
print(l[0])

# 替换目标字符串
s = re.sub(r':', '-', s)
print(s)
