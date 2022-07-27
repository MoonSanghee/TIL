n = int(input())
for line in range(1, n + 1):
    if line % 2 == 1 :
        print('* ' * n)
    else:
        print(' *' * n)