n = int(input())
for _ in range(n):
    password = input()
    if 6 <= len(password) < 10:
        print('yes')
    else:
        print('no')