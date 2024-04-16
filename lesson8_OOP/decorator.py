def average(array):
    # your code goes here
    arr = set(array)
    result = sum(arr) / len(arr)
    return f"{result:.3f}"
    
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)