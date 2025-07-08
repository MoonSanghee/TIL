n = int(input())
result = [0, 10000]
# 진행할 게임의 판수를 받고 결과를 담을 변수를 만들어줍니다 각 판은 n이하의 자연수이고 주어지는 최대 수가 10000이므로 그 범위 밖의 값인 0과 1만을 설쟁해주었습니다
for i in range(n):
    target, limit = map(int, input().split())
    # 주어지는 목표수와 차례마다 부를수 있는 수의 개수를 받아줍니다
    target -= (target - 1) % (limit + 1)
    turns = (target // limit + 1) * 2
    # 게임이 완료되는데 필요한 최소 턴을 구해줍니다
    if turns < result[1]:
        result = [i + 1, turns]
    # 이전의 기록과 비교하여 필요한 턴이 더 적다면 값을 갱신해줍니다
print(*result)
# 결과를 출력해줍니다