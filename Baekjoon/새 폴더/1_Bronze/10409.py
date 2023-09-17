n, t = map(int, input().split())
# 일의 개수와 제한 시간을 받아줍니다.
works = list(map(int, input().split()))
# 순서대로 주어지는 일마다 걸리는 시간을 받아줍니다.
cnt = 0
spend = 0
# 마친 일의 개수와 사용한 시간을 기록할 변수를 설정해줍니다.
for i in range(n):
    spend += works[i]
    # 사용한 시간에 각 차례의 일을 한 시간을 더해줍니다.
    if spend <= t:
        cnt += 1
        # 제한 시간을 넘기지 않았다면 작업을 하나 끝냈다고 표시해줍니다.
    else:
        break
    # 제한 시간을 넘겼다면 더이상 일을 완료할 수 없으므로 반복을 멈추어줍니다.
print(cnt)
# 마친 일의 개수를 출력해줍니다.