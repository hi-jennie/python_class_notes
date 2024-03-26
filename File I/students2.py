import csv

name = input("What's your name?")
owner = input("who do you belong to?")

with open("family.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([name,owner]) #list
    #writer = csv.Dictwriter(file)
    # writer = csv.writer(file,fieldnames=["name","owner"])  ——fieldnames相当于给csv文件设置的heading或者说是结下来输入的key
    # writer.writerow({"name":name,"owner":owner})