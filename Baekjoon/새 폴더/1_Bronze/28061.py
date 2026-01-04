n = int(input())
lemons = list(map(int, input().split()))
# 지나는 나무의 수와 나무마다 있는 레몬의 수를 받아줍니다
for i in range(n):
    lemons[i] -= (n - i)
# 각 나무의 레몬을 주웠을때 집에 도달할때까지 떨어뜨릴 레몬의 수를 구해줍니다
print(max(lemons))
# 가장 많은 레몬을 가져가는 경우를 출력해줍니다