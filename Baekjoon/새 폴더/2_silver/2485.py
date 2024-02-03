from math import gcd

n = int(input())
distance = []
# 심어져있는 가로수의 수와 가로수간의 간격을 담을 변수를 설정해줍니다.
s = int(input())
result = 0
# 첫 나무의 위치를 변수에 담고 심어야하는 나무의 수를 0으로 설정해줍니다.
for _ in range(n - 1):
    e = int(input())
    distance.append(e - s)
    s = e
    # 다음 가로수의 위치를 받고 두 가로수의 거리를 distance에 담고 s값을 갱신해줍니다.
minimum = distance[0]
# 최소 간격을 첫 두 나무간의 거리로 설정해줍니다.
for i in range(1, n - 1):
    minimum = gcd(minimum, distance[i])
    # 모든 거리의 최소 공약수를 확인해줍니다.

for i in distance:
    result += i // minimum - 1
# 각 간격마다 나무를 얼마나 심어야하는지 확인하여 더해줍니다.
print(result)
# 총 심어줘야하는 나무의 수를 출력해줍니다.