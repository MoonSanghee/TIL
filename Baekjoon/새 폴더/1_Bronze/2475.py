numbers = list(map(int, input().split()))
num = 0
for i in numbers:
    num += i ** 2
num %= 10
print(num)