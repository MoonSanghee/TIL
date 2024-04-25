n = int(input())
# 주어진 시간을 받아줍니다.
task, result = [], 0
# 남은 과제와 받을 점수를 담을 변수를 설정해줍니다.
for _ in range(n):
    new = list(map(int, input().split()))
    # 새 과제를 받아줍니다.
    if new[0] == 1:
        task.append((new[1], new[2]))
        # 과제가 주어진다면 과제 목록에 추가합니다.

    if task:
        score, time = task.pop()
        time -= 1
        # 진행해야할 과제가 있다면 가장 마지막에 넣은 과제를 꺼내 점수와 걸리는 시간을 담고 시간을 1만큼 차감시킵니다.
        if time == 0:
            result += score
        else:
            task.append((score, time))
        # 과제를 완료했다면 점수를 추가하고 완료하지 못했다면 과제를 목록에 다시 넣어줍니다.

print(result)
# 최종 획득하는 점수를 출력해줍니다.