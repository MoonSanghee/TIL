result = []

for i in range(200):
    j = i + 1
    if j % 7 == 0 and j % 5 != 0:
        result.append(str(j))

print(','.join(result))