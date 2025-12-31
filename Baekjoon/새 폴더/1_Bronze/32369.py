n, a, b = map(int, input().split())
A, B = 1, 1
# 주어지는 변수를 받고 최초의 양파를 설정해줍니다
for _ in range(n):
    A += a
    B += b
    if B > A:
        A, B = B, A
    elif B == A:
        B -= 1
# n일동안 실험을 진행하여줍니다
print(A, B)
# 결과를 출력해줍니다