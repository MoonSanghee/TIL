n = int(input())
trees = list(map(int, input().split()))
trees.sort(reverse = True)
num = []
for i in range(n):
    result = trees[i] + i + 2
    num.append(result)
print(max(num))