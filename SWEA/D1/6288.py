result = []
for i in range(1, 21):
    if i % 3 != 0 or i % 5 != 0:
        result.append(i * i)

print(result)