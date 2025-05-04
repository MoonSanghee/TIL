import heapq
n = int(input())
snows = list(map(int, input().split()))
flag = True
cnt = 0
# 주어지는 변수들을 받아줍니다
# 필요한 시간을 담을 변수와 24시간 이상 필요한 집이 있는지 확인할 변수를 설정해줍니다
for i in range(n):
    if snows[i] > 1440:
        flag = False
    snows[i] *= -1
snows.sort()
# 각 집의 눈 값을 확인해 24시간 이상 필요한 집이 있다면 표시하고 모든 값을 -1을 곱하여 넣은 다음 리스트를 정렬해줍니다
if flag == False:
    print(-1)
    # 모든 눈을 녹일수 없다면 -1을 출력해줍니다
else:
    while len(snows) > 0:
        x = -heapq.heappop(snows)
        if snows:
            y = -heapq.heappop(snows)
            heapq.heappush(snows, -(x - y))
            cnt += y
        else:
            cnt += x
    # 리스트에 남은 눈 덩이가 없어질 때 까지 가장 큰 더미가 남은 두 집 중 작은 더미만큼 시간을 더하고 
    # 큰 더미에서 작은더미를 뺀 다음 다시 리스트에 넣어줍니다
    if cnt > 1440:print(-1)
    else:print(cnt)
    # 필요한 시간이 24시간 이상이라면 -1 아니라면 필요한 시간을 출력해줍니다