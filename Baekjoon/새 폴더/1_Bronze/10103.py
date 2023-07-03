Jeongsoo, Sangdeok = 100, 100
# 정수와 상덕이의 기본 점수를 세팅해줍니다.
n = int(input())
# 주사위를 몇 번 굴리는지 받아줍니다.
for _ in range(n):
    a, b = map(int, input().split())
    # 주사위를 굴리며 둘이 가진 수를 받아줍니다.
    if a > b :
        Sangdeok -= a
        # 정수의 값이 크면 상덕이의 점수에서 그 값을 빼주고
    elif b > a:
        Jeongsoo -= b
        # 상덕이의 값이 크면 정수의 점수에서 그 값만큼 빼줍니다.

print(Jeongsoo)
print(Sangdeok)
# 정수와 상덕이의 점수를 차례대로 출력해줍니다.