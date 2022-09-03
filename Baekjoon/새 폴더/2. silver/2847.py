n = int(input())
numbers = []
for i in range(n):
    number = int(input())
    numbers.append(number)
numbers = numbers[::-1]
result = 0
for i in range(n - 1):
    if numbers[i] <= numbers[i + 1]:
        result += numbers[i + 1] - numbers[i] + 1
        numbers[i + 1] = numbers[i] - 1
print(result)