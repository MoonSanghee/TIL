n = int(input())
for i in range(n):
    word = ' ' * (n - i - 1) + '*' * (2 * i + 1)
    print(word)

for i in range(1, n):
    word = ' ' * i + '*' * (2 * (n - i) - 1)
    print(word)