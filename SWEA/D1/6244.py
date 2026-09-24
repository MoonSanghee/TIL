li = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
result = 0

while li:
    x = li.pop()
    if x >= 80:
        result += x

print(result)