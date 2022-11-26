n = int(input())

s = 0
e = n

while s <= e:
    mid = (s + e) // 2
    if mid ** 2 < n:
        s = mid + 1
    else:
        e = mid - 1
# 이분탐색을 통해 주어진 수의 중앙값이 제곱근이 될때까지 반복하여 답을 구하였습니다.
print(s)