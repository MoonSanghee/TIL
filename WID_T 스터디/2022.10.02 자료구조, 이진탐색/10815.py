n = int(input())
N = list(map(int, input().split()))
N = sorted(N)
m = int(input())
M = list(map(int, input().split()))

for i in M:
    low, high = 0, n - 1
    check = 0
    while low <= high:
        mid = (low + high) // 2
        if N[mid] > i:
            high = mid - 1
        elif N[mid] < i:
            low = mid + 1
        else:
            check = 1
            break
    print(check, end = ' ')