from itertools import permutations
str_,times = input().split(" ")

print_str = []
for i in permutations(str_,int(times)):
    print_str.append("".join(i))

for i in sorted(print_str):
    print(i)