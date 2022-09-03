n = int(input())
numbers = list(map(int, input().split()))
check = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j] and check[i] < check[j]:
            check[i] = check[j]
    check[i] += 1
print(max(check))