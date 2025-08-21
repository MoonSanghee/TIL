n, k = map(int, input().split())
arr = list(map(int, input().split()))
# 코스의 구간 개수와 이동한 거리 코스의 위치를 받아줍니다의
for i in range(n):
    k -= arr[i]
    if k < 0:
        print(i + 1)
        break
    # 코스의 끝까지 가면서 이동이 완료되었는지 확인하여완료되었다면 어느 구간인지 출력해줍니다
else:
    for i in range(n - 1, -1, -1):
        k -= arr[i]
        if k < 0:
            print(i + 1)
            break
    # 복귀하며 이동이 완료되었는지 확인하여 어느 구간까지 이동하였는지 출력해줍니다