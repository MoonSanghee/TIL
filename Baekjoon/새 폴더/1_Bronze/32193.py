n = int(input())
A, B = 0, 0
# 높이와 깊이를 담을 변수를 설정해줍니다
for _ in range(n):
    a, b = map(int, input().split())
    A += a
    B += b
    print(A - B)
    # 고저의 변화를 받아 더하고 그 차이를 출력해줍니다