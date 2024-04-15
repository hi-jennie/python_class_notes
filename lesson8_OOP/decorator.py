
import math
import os
import random
import re
import sys
    
# Complete the solve function below.
def solve(s)：
    words = re.findall(r'\b\w+\b|\s+', s)
    result = [word.capitalize() if word.isalpha() else word for word in words]
    return " ".join(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

