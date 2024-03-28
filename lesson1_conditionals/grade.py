# 给分数划分等级

score = int(input("score: "))


"""
if 90 <= score <= 100:
    print("Grade:A ")
    
elif 80 <= score <90:
    print("Grade:B ")
    
elif 70 <= score <80:
    print("Grade:C ")
"""

if score >= 90:
    print("Grade:A ")
elif score >= 80:
    print("Grade:B ")
elif score >= 70:
    print("Grade:C ")

# 因为已经检查过分数是否大于90 ，所以执行到第二步，其实自带一个条件小于90
# 执行到第三步已经自带条件分数小于90 ，分数小于80.所以只需要问一个问题即可。
