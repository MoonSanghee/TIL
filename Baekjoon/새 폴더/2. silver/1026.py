s = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a)
b = sorted(b, reverse = True)
number = 0
for i in range(s):
    number += a[i] * b[i]
print(number)