def closest_number(arr,target):
    d = abs(target - arr[0])
    ele = arr[0]
    
    for i in arr:
        diff = abs(target - i)
        if diff < d:
            d = diff
            ele = i
    return ele

arr = list(map(int, input().split()))
target = int(input())

print(closest_number(arr,target))