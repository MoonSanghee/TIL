n = int(input())
numbers = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i, 0, -1):
        if numbers[j] < numbers[j - 1]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
        else:
            break
for i in range(1, n):
    numbers[i] += numbers[i - 1]
print(sum(numbers))