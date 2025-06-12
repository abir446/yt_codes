def generate_subarrays(A, ans, temp, index, n):
    if index == n:
        ans.append(temp[:])
        return

    generate_subarrays(A, ans, temp, index + 1, n)
    temp.append(A[index])
    generate_subarrays(A, ans, temp, index + 1, n)
    temp.pop()

n = int(input())
A = list(map(int, input().split()))
ans = []
temp = []

generate_subarrays(A, ans, temp, 0, n)

for sub in ans:
    print(*sub)
