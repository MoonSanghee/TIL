n = int(input())
w = int(input())
# 방문한 명소의 수와 걸음수를 받아줍니다
score = n * 10
# 방문한 명소의 수에 따라 주어지는 점수를 받아줍니다
if n == 5:
    score += 70
elif n >= 3:
    score += 20
# 주어지는 추가점수를 더해줍니다
if w > 1000:
    score -= 15
    if score < 0:
        score = 0
# 감점을 확인해줍니다
print(score)
# 결과를 출력해줍니다