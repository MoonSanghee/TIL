n, m = map(int, input().split())
numbers = list(map(int, input().split()))
start = 0
end = 0
result = 0
cnt = 0
while end < n:
    result += numbers[end]
    while result > m:
        result -= numbers[start]
        start += 1
    if result == m:
        cnt += 1
    end += 1
print(cnt)