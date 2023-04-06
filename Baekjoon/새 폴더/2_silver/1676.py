n = int(input())
result = 1
for i in range(1, n + 1):
    result *= i
cnt = 0
while True:
    if result % 10 == 0:
        cnt += 1
        result //= 10
    else:
        break
print(cnt)