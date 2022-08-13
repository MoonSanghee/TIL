n = int(input())
numbers = []
for i in range(n):
    number = int(input())
    numbers.append(number)
numbers = sorted(numbers, reverse = True)
result = []
for i in range(n):
    result.append(numbers[i]* (i + 1))
print(max(result))