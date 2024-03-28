#上下文管理器——with 在书129页，使用上下文管理器可以 close automatically


'''
name = input("What's your name?")
#打开names.txt为编辑（write）模式
#file = open("names.txt","w")
file = open("names.txt","a") #a是append
#在其中写入name这个变量
file.write(f"{name}\n")
file.close()


#使用上下文管理器
name = input("What's your name?")

with open("names.txt","a") as file:
    file.write(f"{name}\n")
   

with open("names.txt","r") as fp:
    lines = fp.readlines()
for line in lines:
    print("hello,", line.rstrip()) #rstrip处理多余的换行
'''   

#sorted 文件中的内——如果对想对读取出来的文件做处理，可以先将读取出来的内容用一个空的变量装起来，再做其他处理
names = []

with open("names.txt","r") as fp:
    for line in fp:
            names.append(line.rstrip())
            
for name in sorted(names,reverse = True):
    print(f"hello, {name}")

#简化后
'''
with open("names.txt","r") as fp:
    for line in sorted(fp):
        print(f"hello, ", line.rstrip())
'''