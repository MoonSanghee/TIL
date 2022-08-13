n = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)
result = 0
time = 0
for i in range(n):
    time += numbers[i]
    result += time
print(result)