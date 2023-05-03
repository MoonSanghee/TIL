t = int(input())
for tc in range(t):
    result = 0
    n = int(input())
    for _ in range(n):
        result += int(input())
    if result > 0:
        print('+')
    elif result == 0:
        print('0')
    else:
        print('-')