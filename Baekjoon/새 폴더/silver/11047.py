n, k = list(map(int, input().split()))
numbers = []
for i in range(n):
    number = int(input())
    numbers.append(number)
numbers = sorted(numbers, reverse = True)

cnt = 0
for i in numbers:
    cnt += (k // i)
    k %= i
    if k == 0:
        break
print(cnt)