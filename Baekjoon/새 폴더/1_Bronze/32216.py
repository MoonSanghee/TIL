n, k, t = map(int, input().split())
d = [0] + list(map(int, input().split()))
arr = [t] + [0] * n
# 주어지는 변수를 받아줍니다
for i in range(n):
    if arr[i] > k:
        arr[i + 1] = arr[i] + d[i + 1] - abs(arr[i] - k)
    elif arr[i - 1] < k:
        arr[i + 1] = arr[i] + d[i + 1] + abs(arr[i] - k)
    else:
        arr[i + 1] = arr[i] + d[i + 1]
# 조절을 담아줍니다
result = 0
for i in arr[1:]:
    result += abs(i - k)
# 불쾌감 지수를 더해줍니다
print(result)
# 결과를 출력해줍니다