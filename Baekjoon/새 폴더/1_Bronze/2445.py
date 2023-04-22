n = int(input())

for i in range(1, n):
    row = '*' * i + ' ' * (n - i) + ' ' * (n - i) + '*' * i
    print(row)
print('*' * 2 * n)
for i in range(1, n):
    row = '*' * (n - i) + ' ' * i + ' ' * i + '*' * (n - i)
    print(row)