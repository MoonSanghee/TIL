i, j, x, y = map(int, input().split())
check = [i, j, x - i, y - j]
print(min(check))