
#x =[36.65/235.30, 41.93/259.32, 42.86/275.54, 44.48/276.88]
#for i in x:
#    c =round(i, 3)
#    print(c)

original_list = [3.88,	3.79,	3.88,	3.75,	3.73]
min = min(original_list)
max = max(original_list)
print(min, max)

for i in original_list:
    x = max - i
    y = max - min
    n = x/y + 0.0001
    print(round(n, 4))
   
    