t = int(input())

for tc in range(t):
    n = int(input())
    result = ''
    while True:
        if n >= 5:
            result += '++++ '
            n -= 5
        elif n > 0:
            result += '|'
            n -= 1
        else:
            print(result)
            break