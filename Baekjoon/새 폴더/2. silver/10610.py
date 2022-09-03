number = int(input())
numbers = sorted(list(str(number)), reverse = True)
if number % 3 == 0 and '0' in numbers:
    for i in numbers:
        print(i, end = '')
else:
    print(-1)