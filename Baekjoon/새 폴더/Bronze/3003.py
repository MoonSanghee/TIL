check = [1, 1, 2, 2, 2, 8]

call = list(map(int, input().split()))

for i in range(len(check)):
    print(check[i] - call[i], end = ' ')
