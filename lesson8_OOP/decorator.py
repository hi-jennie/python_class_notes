from collections import defaultdict
d = defaultdict(list)
g, s = input().split()
word = []
subword = []

while int(g) > 0:
    alpha = input()
    word.append(alpha)
    g = int(g) - 1
    
while int(s) > 0:
    alpha = input()
    subword.append(alpha)
    s = int(s) - 1

group = {}
for i, alpha in enumerate(word,start=1):
    group[i] = alpha

for i in subword:
    if i in group.values():
        for j in group:
            if group[j] == i:
                d[i].append(j)
    else:
        d[i].append(-1)
            
    

for value in d.values():
    for i in value:
        print(i,end=" ")
    print()   