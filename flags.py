"""
flags 扩展演示
"""
import re

s = """Hello
北京 
"""

# # 只能匹配ASCII编码
# regex = re.compile(r'\w+', flags=re.ASCII)

# # 不区分大小写
# regex = re.compile(r'[a-z]+', re.IGNORECASE)

# # 可以匹配换行
# regex = re.compile(r'.+', re.DOTALL)

# # ^,$ 匹配每一行开头结尾位置
# regex = re.compile(r'^北京', re.MULTILINE)

# 为正则表达式增加多行注释
pattern = r"""
\w+  # hello
\s+  # 匹配换行
\w+  # 北京
"""
# regex = re.compile(r'\w+\s+\w+')
regex = re.compile(pattern, re.VERBOSE)

l = regex.findall(s)
print(l)





