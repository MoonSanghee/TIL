n = int(input())
for i in range(n):
    stars = ' ' * (n - i - 1) + '*' * (i * 2 + 1)
    print(stars)