n, m = map(int, input().split())
numbers = list(map(int, input().split()))
check = [0]
sum_n = 0
for i in numbers:
    sum_n += i
    check.append(sum_n)

for _ in range(m):
    i, j = map(int, input().split())
    print(check[j] - check[i - 1])