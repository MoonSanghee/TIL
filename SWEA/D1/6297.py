li = list(map(int, input().split(',')))
result = []

for i in li:
    if i % 2:
        result.append(i)

for i in range(len(result) - 1):
    print(result[i], end = ', ')

print(result[-1])