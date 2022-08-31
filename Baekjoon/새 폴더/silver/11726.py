n = int(input())
numbers = [0] * (n + 1)
numbers[1] = 1
numbers[2] = 2
for i in range(3, n + 1):
    numbers[i] = numbers[i - 1] + numbers[i - 2]

result = numbers[-1]%10007
print(result)