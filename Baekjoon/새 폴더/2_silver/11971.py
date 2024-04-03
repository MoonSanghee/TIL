n, m = map(int, input().split())
road = []
result = 0
# 나뉘는 구간의 수를 받고 도로의 제한 속도를 담을 리스트형 변수와 결과를 담을 정수형 변수를 정해줍니다.
for _ in range(n):
    distance, limit = map(int, input().split())
    for _ in range(distance):
        road.append(limit)
# 구간변 제한속도를 받아 roads 리스트에 담아줍니다.
        
passed = 0
# 지난 자리의 제한 속도를 확인하기 위한 인덱스 값을 담을 정수형 변수를 설정해줍니다.
for _ in range(m):
    drive, speed = map(int, input().split())
    for i in range(drive):
        over = speed - road[passed]
        result = max(result, over)
        passed += 1
# 지나온 자리를 확인하며 제한 속도를 어겼다면 값을 갱신해줍니다.
print(result)
# 결과를 출력해줍니다.