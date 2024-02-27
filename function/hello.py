name = input("what't your name?").strip().title()

#split user's name into first name and last name
first,last = name.split(" ")


#remove whitespace from str
#name = name.strip()

#capitalize user's name
#name = name.capitalize()
#name = name.title()


#合并前两个命令
#name = name.strip().title()


#1. print("hello, ", end='')  #python默认自动分行
#print(name)


#2. print("hello," + name)----
#"+"de 是连接name这个变量到“hello，”这个string中,也可以用“，”进行连接 

#3. print("hello,", name, sep="???")   
# “，”使用逗号也可以传argument，而且可以传多个arguments
#默认情况下前两个参数的sep（间隔）是一个空格“ ”。

print(f"hello, {first}")
#f是提醒计算机这个一个特殊的string，就可以在“”里面加{}的variable