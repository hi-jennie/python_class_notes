n,m =input().split()
n, m = int(n),int(m)

line = 1
len1 = int(1)
len2 = int((m - 3*len1)/2)
line_middle = (m-7)/2

while True:
    a = len2 * "-"
    b = len1 * ".|."
    if line < (n+1)/2:
        print(f"{a}{b}{a}")
        line +=1
        len1 +=2
        len2 -=3
        
    elif line == (n+1)/2:
        middle = int(line_middle) * "-"
        print(f"{middle}WELCOME{middle}")
        line +=1
        len1 -=2
        len2 +=3
   
    elif (n+1)/2 < line < n+1 :
        
        print(f"{a}{b}{a}")
        line +=1
        len1 -=2
        len2 +=3
    else:
        break
    

        



