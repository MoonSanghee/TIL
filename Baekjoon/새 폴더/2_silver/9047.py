n = int(input())

for _ in range(n):
    number = int(input())
    cnt = 0

    while True:
        if number == 6174:
            break
        cnt += 1
        line = list(str(number))
        number = int(''.join(sorted(line, reverse=True))) - int(''.join(sorted(line)))

        # while number < 1000:
        #     number *= 10
    print(cnt)