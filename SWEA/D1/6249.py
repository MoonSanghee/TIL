n = input()

numbers = [0] * 10
for i in n:
    numbers[int(i)] += 1

for i in range(10):
    print(i, end=' ')
print()
print(*numbers)