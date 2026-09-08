result = [[] for _ in range(8)]

for i in range(8):
    for j in range(1, 10):
        n = i + 2
        if n * j % 3 != 0 and n * j % 7 != 0:
            result[i].append(n * j)

print(result)