import string

n = int(input())
m = 0
lowercase_letters = list(string.ascii_lowercase)
print_list = []

while m < n:
    middle_list = lowercase_letters[m:n]
    middle_list.reverse()
    middle_list = middle_list + (lowercase_letters[m + 1 : n])
    print_list.append(middle_list)
    m += 1

former_part = print_list.copy()
former_part.reverse()
new_list = former_part[: n - 1] + print_list
for i in new_list:
    print("-".join(i).center(4 * n - 3, "-"))
