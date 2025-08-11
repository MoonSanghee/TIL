n = int(input())
ranks = [list(map(int, input().split())) for _ in range(n)]
# 참가하는 선수의 수를 받고 성적을 받아줍니다
ranks.sort(key = lambda x : (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]))
# 세 종목 순위의 곱, 합, 등번호순 오름차순으로 정렬해줍니다
for i in range(3):
    print(ranks[i][0], end = ' ')
# 금, 은, 동메달을 받을 선수의 번호를 출력해줍니다