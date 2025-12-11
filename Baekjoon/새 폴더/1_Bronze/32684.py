points = [13, 7, 5, 3, 3, 2]
result = 1.5
# 각 기물의 점수와 한의 기본점수를 결과에 담아줍니다
cho = list(map(int, input().split()))
han = list(map(int, input().split()))
# 초와 한 나라의 남은 기물의 개수를 받아줍니다
for i in range(6):
    result += han[i] * points[i]
    result -= cho[i] * points[i]
# 한의 점수는 더하고 초의 점수는 빼줍니다
if result > 0:
    print("ekwoo")
else:
    print("cocjr0208")
# 점수가 양수이면 한이 음수이면 초가 승리하였다고 출력해줍니다