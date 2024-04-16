n = int(input())
A, B = 0, 0
# 결과를 담을 변수를 설정해줍니다.
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        A += 1
    elif b > a:
        B += 1
# 결과를 확인하고 갱신해줍니다.
print(A, B)
# 결과를 차례대로 출력해줍니다.