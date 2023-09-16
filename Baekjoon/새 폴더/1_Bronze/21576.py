n = int(input())
arr = [i + 1 for i in range(n)]
while len(arr) > 1:
    arr2 = []
    for a in arr[1::2]:
        arr2.append(a)
    arr = arr2

print(*arr)