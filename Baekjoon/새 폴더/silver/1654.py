k, n = map(int, input().split())
numbers = []
for i in range(k):
    numbers.append(int(input()))

s, e = 1, max(numbers)
while s <= e:
    mid = (s+e)//2
    cnt = 0
    for i in numbers:
        cnt += i//mid
    if cnt >= n:
        s = mid + 1
    else:
        e = mid - 1
print(e)