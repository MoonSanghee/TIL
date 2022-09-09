n = int(input())
numbers = [0 for _ in range(n + 1)]
numbers[1] = 1
numbers[2] = 2
for i in range(3, n + 1):
    numbers[i] = (numbers[i - 1] + numbers[i - 2]) % 15746
print(numbers[-1])