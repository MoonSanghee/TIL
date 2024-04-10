n,m = map(int, input().split())
player = []
answer = [0] * n
result = []
# 플레이어의 수와 카드, 점수, 최고점자를 담을 변수를 설정해줍니다.

for i in range(n):
    tmp = sorted(list(map(int, input().split())))
    player.append(tmp)
# 각 차례마다 높은 카드순으로 낼것이므로 카드를 정렬하여 각 플레이어가 가진 카드를 정렬해줍니다.

for i in range(m):
    open = []
    for j in range(n):
        open.append(player[j][i])
    high = max(open)
    for j in range(n):
        if high == open[j]:
            answer[j] += 1
# 각 차례마다 가장 높은 카드를 확인하여 점수를 획득하는 플레이어를 표시해줍니다.

winner = max(answer)
for i in range(n):
    if answer[i] == winner:
        result.append(i+1)
print(*result)
# 최고점자를 찾아 리스트에 담고 리스트에 담긴 값들을 출력해줍니다.