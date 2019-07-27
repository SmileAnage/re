"""
regex1 re模块 功能函数演示3
生成match对象的函数
"""
import re

s = "今年是2019年,建国70周年"

pattern = r'\d+'

# 返回可迭代对象
it = re.finditer(pattern, s)

# 可遍历对象，需用for循环打印结果
for i in it:
    print(i)  # 获取match对象对应内容

# 完全匹配一个字符串
m = re.fullmatch(r'[,\w]+', s)
print(m)

# 匹配开始位置
m = re.match(r'[\w]+?', s)
print(m)

# 匹配第一处符合正规规则的内容
m = re.search(r'\d', s)
print(m)
