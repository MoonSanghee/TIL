import sys
input = sys.stdin.readline

n, t = map(int, input().split())
carrots = [list(map(int, input().split())) for _ in range(n)]
# 당근의 개수와 몇일간 재배할지를 받고 당근과 영양제 정보를 받습니다.
total = 0
carrots.sort(key = lambda x : x[1])
# 총 당근의 맛을 담을 변수를 만들고 당근을 영양제 효과를 기준으로 오름차순으로 정렬해줍니다.
for i in range(n):
    total += carrots[i][0] + (t - n + i) * carrots[i][1]
# 영양제로 증가하는 맛이 당근을 새로 심는 맛 이상이고 당근을 재배하는 일수가 심는 당근 이상입니다.
# 따라서 모든 당근은 최대한 영양제를 만이 주고 먹는것이 가장 큰 맛을 느낄수 있으므로 모든 당근을 최대한 놔두었다가 먹는 값을 total에 더해줍니다.
print(total)
# total 값을 출력해줍니다.