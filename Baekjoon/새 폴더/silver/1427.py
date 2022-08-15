word = str(input())
num = dict()

for i in word:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1
for i in range(10):
    if str(9 - i) in num:
        print(str(9 - i) * num[str(9 - i)], end = '')