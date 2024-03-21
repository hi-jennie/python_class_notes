groceries = []

while True:
    try:
        grocery = input()
        groceries.append(grocery)
    except (KeyboardInterrupt, EOFError):
        break

groceies_times = {}
for item in groceries:
    if item in groceies_times:
        groceies_times[item] += 1
    else:
        groceies_times[item] = 1


"""for grocery,times in sorted(groceies_times).items():  
    print(times, grocery.upper())
    sorted(groceies_times).items() 这部分是错误的。sorted() 函数会返回一个排序后的列表，而不是字典，所以它没有 items() 方法。
"""
for grocery in sorted(
    groceies_times
):  # 这一行的grocery其实是字典当中排好顺序的键。sorted(groceies_times) 会返回一个包含字典所有键的排序后的列表。然后，我们可以使用这些键来获取对应的值。
    times = groceies_times[grocery]
    print(times, grocery.upper())
