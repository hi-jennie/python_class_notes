#文件扩展名 (ext)，媒体类型 (mime_type)/   folder.items(): 表示遍历字典 folder 中的所有键值   /endswith(ext)检查文件名是否以给定的后缀 ext 结尾


file_name = input("filename:").strip()

folder = {
".gif":"image/gif",
".jpg":"image/jpeg",
".jpeg":"image/jpeg",
".png":"image/png",
".pdf":"application/pdf",
".txt":"text/plain",
".zip":"application/zip"
}
"""
自己的错误写法🙅😭，难顶嗷

for i in folder:
    if i in file_name:
        print(folder[i])
        break
    else:
        print("application/octet-stream")
"""       


for ext, mime_type in folder.items():
    if file_name.lower().endswith(ext):
        print(mime_type)
        break
else:
    print("application/octet-stream")
    
"""
    
for 关键字表示开始一个循环。
ext, mime_type 是两个变量，用于接收字典中的键和对应的值。
in folder.items(): 表示遍历字典 folder 中的所有键值对
.endswith(ext) 是一个字符串方法，用于检查文件名是否以给定的后缀 ext 结尾。如果文件名以 ext 结尾，返回 True。否则，返回 False。
for example:

file_name = "document.txt"
ext = ".txt"

if file_name.lower().endswith(ext):
    print("该文件是文本文件")
else:
    print("文件格式未知")
"""