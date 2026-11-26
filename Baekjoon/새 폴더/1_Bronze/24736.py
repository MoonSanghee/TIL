first = list(map(int, input().split()))
second = list(map(int, input().split()))
point = [6, 3, 2, 1, 2]

for i in range(5):
    first[i] *= point[i]
    second[i] *= point[i]

print(sum(first), sum(second))