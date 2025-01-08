n = int(input())
condos = sorted([list(map(int, input().split())) for _ in range(n)])
# 정보가 주어지는 콘도의 수와 콘도의 정보를 받고 콘도를 거리를 기준으로 정렬해줍니다
cost = 10001
cnt = 0
# 비교할 비용과 조건에 맞는 콘도의 수를 담을 변수를 설정해줍니다
for d, c in condos:
    if c < cost:
        cnt += 1
        cost = c
# 콘도의 정보를 순회하며 비용이 더 저렴하다면 조건을 만족하므로 cnt 값을 더해주고 cost 값을 갱신해줍니다

print(cnt)
# 결과를 출력해줍니다