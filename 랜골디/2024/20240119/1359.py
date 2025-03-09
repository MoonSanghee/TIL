from itertools import combinations

n, m, k = map(int,input().split())
# 세 정수를 받아줍니다.
ans = 0
# k개의 수가 일치하는 조합의 수를 담을 변수를 설정해줍니다.
coms = [*combinations([i for i in range(n)], m)]
# 조합을 구해줍니다.

for com in coms:
  cnt = 0
#   당첨 조합과 비교하여 일치하는 수를 확인할 변수를 만들어줍니다.
  for j in range(m):
    if com[j] < m:
      cnt += 1
    #   임의의 당첨 번호에 포함되면 일치하는 번호의 수를 더해줍니다
  if cnt >= k:
    ans += 1
    # 일치하는 공의 수가 충분하다면 ans의 값을 1 증가시켜줍니다.

print(ans / len(coms))
# 일치하는 조합의 수를 전체 조합으로 나눈 값을 출력해줍니다.