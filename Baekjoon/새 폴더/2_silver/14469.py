n = int(input())
cows = []
for _ in range(n):
    cows.append(list(map(int, input().split())))
cows.sort(key=lambda x : (x[0], x[1]))
# 도착할 소의 마리수를 받고 리스트에 소가 도착하는 시간과 검문받는데 걸리는 시간을 리스트로 묶어 빈 리스트에 담아줍니다.
# 그리고 소가 도착하는 시간과 걸리는 시간 순으로 정렬하여줍니다.

result = 0
for i in range(n):
    if cows[i][0] >= result:
        result = cows[i][0] + cows[i][1]
    else:
        result += cows[i][1]
    # 검문중에 소가 도착하면 검문에 걸리는 시간을 그냥 더해주고 검문이 완료된 다음 
    # 소가 도착하였다면 소가 도착한 시간에 검문에 걸리는 시간을 더해서 검문이 끝나는 시간을 result에 담아줍니다.

print(result)
# 모든 소가 입장하는데 필요한 시간을 출력해줍니다.