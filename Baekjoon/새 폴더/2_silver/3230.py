n, m = map(int, input().split())
# 전체 참가자 n명과 2차 시도를 할 m명을 받아줍니다.
ranks = []
for i in range(1, n + 1):
    p = int(input())
    if len(ranks) < p:
        ranks.append(i)
    else:
        ranks.insert(p - 1, i)
# 전체 참가자 n명의 1차 결과를 리스트에 담아줍니다.
ranks = ranks[:m]
# 2차 점프를 할 m명까지 잘라줍니다.

finish = []
for _ in range(m):
    number = ranks.pop()
    p = int(input())
    if len(finish) < p:
        finish.append(number)
    else:
        finish.insert(p - 1, number)
# 최종 결과를 담을 리스트를 만들고 m명의 2차 점프 결과를 담아줍니다.

for i in range(3):
    print(finish[i])
# 금, 은, 동메달을 수상할 선수를 출력해줍니다.