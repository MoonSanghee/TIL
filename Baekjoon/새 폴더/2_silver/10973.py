n = int(input())
numbers = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if numbers[i - 1] > numbers[i]:
        target = i - 1
        break
else:
    print(-1)
    exit()
    
for i in range(n - 1, 0, -1):
    if numbers[i] < numbers[target]:
        numbers[i], numbers[target] = numbers[target], numbers[i]
        break
numbers = numbers[:target+1] + sorted(numbers[target+1:], reverse = True)
print(*numbers)