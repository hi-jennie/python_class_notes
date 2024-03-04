import re
before = input("camelcase:")

find_upper = re.findall('[A-Z]', before)
#re.findall(pattern, string, flags=0)：在字符串 string 中查找所有与正则表达式 pattern 匹配的非重叠子串。
# 如果 pattern 中存在一个或多个捕获组，返回一个组合列表；如果 pattern 有多个组，结果将是一个元组的列表。空匹配也会包含在结果中。

for f in find_upper:
    before = before.replace(f"{f}",f"_{f}")

after = before.lower()
print(f"snake_case:{after}")