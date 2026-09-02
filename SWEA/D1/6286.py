result = [1,1]
while len(result) < 10:
    result.append(result[-2] + result[-1])

print(result)