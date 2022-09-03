n = int(input())
fivem = n // 300
n %= 300
min = n // 60
n %= 60
tens = n //10
n %= 10
if n == 0:
    print(fivem, min, tens)
else:
    print(-1)