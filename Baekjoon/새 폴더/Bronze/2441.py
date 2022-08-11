stars = int(input())
for i in range(stars):
    print(' ' * i, end = '')
    print('*' * (stars - i))