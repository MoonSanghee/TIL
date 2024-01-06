n = int(input())
works = [tuple(map(int, input().split())) for _ in range(n)]
# 작업의 수와 작업을 튜플로 받아 리스트에 담아줍니다.
works.sort(key = lambda x : x[1])
# 작업을 끝내야하는 시간을 기준으로 정렬해줍니다.
need, end = works.pop()
end_time = end - need
# 가장 늦게 끝내도 괜찮은 작업을 끝내는 시간을 담아줍니다.
finish = True
# 끝낼수 있는지 를 불리언으로 담아줍니다.
while works:
    # 모든 작업을 완료할때까지 실행해줍니다.
    need, end = works.pop()
    # 작업을 꺼내서 변수에 받아줍니다.
    if end > end_time:
        end_time -= need
    else:
        end_time = end
        end_time -= need
    # 마감시한이 이전 작업을 끝낸 시간보다 뒤라면 지금까지 작업을 끝낸 시간에 바로 작업하는데 필요한 시간을 빼주고
    # 마감시한이 이전 작업을 끝낸 시간보다 앞이라면 마감시한을 갱신하고 작업 시간을 빼줍니다.
    if end_time < 0:
        finish = False
        break
    # 마감시한이 음수가 된다면 작업을 끝낼수 없으므로 끝낼수 없다고 표시하고 반복을 멈추어줍니다.

if finish:
    print(end_time)
else:
    print(-1)
    # 작업을 끝낼수 있는지 확인하여 값을 출력해줍니다.