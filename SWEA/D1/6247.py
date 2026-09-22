n = 0

while n < 4:
    stars = ' ' * n + '*' * (7 - 2 * n) + ' ' * n
    print(stars)
    n += 1