n = int(input())

for i in range(5):
    for _ in range(n):
        if i % 2 == 0:
            print('@' * (5 * n))
        else:
            print('@' * n)