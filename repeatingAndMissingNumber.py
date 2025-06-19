def repeatingAndMissingNumber(arr):
    n = len(arr)
    hash = [0] * (n + 1)
    repeating = -1
    missing = -1
    for i in range(n):
        hash[arr[i]] += 1
    
    for i in range(1, n + 1):
        if hash[i] == 2:
            repeating = i
        elif hash[i] == 0:
            missing = i
    return [repeating, missing]

arr = list(map(int,input().split()))
print(repeatingAndMissingNumber(arr))