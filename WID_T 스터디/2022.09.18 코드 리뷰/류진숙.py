# 백준 1855
n = int(input())
sen = input()
a = ['' for i in range(len(sen) // n)]
for i in range(len(sen) // n):
    if i % 2 == 0:
        a[i] = sen[i * n : (i + 1) * n]
    else:
        a[i] = sen[(i + 1) * n - 1:i * n - 1: -1]

for i in range(n):
    for j in range(len(sen) // n):
        print(a[j][i], end='')
