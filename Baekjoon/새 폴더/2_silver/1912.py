n = int(input())
numbers = list(map(int, input().split()))
best = [numbers[0]]
for i in range(n - 1):
    best.append(max(best[i] + numbers[i + 1], numbers[i + 1]))
print(max(best))