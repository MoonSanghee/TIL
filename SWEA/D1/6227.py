result = []

for i in range(100, 301):
    i = str(i)
    for j in i:
        if int(j) % 2:
            break
    else:
        result.append(i)

print(','.join(result))