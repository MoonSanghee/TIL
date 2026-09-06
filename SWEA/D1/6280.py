n = int(input())
result = []

for i in range(n):
    if n % (i + 1) == 0:
        result.append(i + 1)

print(result)