import re
 #re.sub()5个参数
 
url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# ————这种情况下无法做bool值判断,当输入“https://www.google.com/"的网址时就不行，就是当无法找到要背替换的值会出错

matches = re.search(r"^(https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$ ", url, re.IGNORECASE)  # 最后的(.+)表示capture
#(?:www\.)表示不捕捉（）里面的东西，只表示这是一个group
if matches:
    print(matches.group(1))
