a, b, c = map(int, input().split())
n = int(input())
result = 0
# 풀이 방식별 점수와 참가 동아리의 수를 받고 결과를 담을 변수를 설정해줍니다
for _ in range(n):
    point = 0
    # 동아리의 점수를 담을 변수를 설정해줍니다
    for _ in range(3):
        x, y, z = map(int, input().split())
        point += x * a + y * b + z * c
    # 동아리원의 점수를 더해줍니다
    result = max(result, point)
    # 최고점인지 확인하여 값을 갱신해줍니다
print(result)
# 결과를 출력해줍니다