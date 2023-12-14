n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

target = 0

for i in numbers:
    if target + 1 < i:
        break
    target += i
print(target + 1)