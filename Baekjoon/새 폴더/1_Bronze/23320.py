n = int(input())
score = list(map(int, input().split()))
x, y = map(int, input().split())
# 학생수와 학생들의 성적, 상대평가에서 A의 비율과 절대평가 기준점수를 받아줍니다.
cnt = 0
for i in score:
    if i >= y:
        cnt += 1
# 절대평가를 통과하는 학생을 확인해줍니다.

print(f'{round(n * (x / 100))} {cnt}')
# 결과를 출력해줍니다.