n, q = map(int, input().split())
spend = [0 for _ in range(n + 1)]
# 살아온날과 쿼리의 개수를 받고 살아온 날 길이 의 소비를 담을 리스트를 만듭니다.
for _ in range(q):
    query, p, x = map(int, input().split())
    # 주어지는 쿼리와 입력값들을 받아줍니다.
    if query == 1:
        spend[p] += x
    else:
        print(sum(spend[p:x + 1]))
    # 쿼리가 1이라면 소비를 갱신해주고 2라면 주어지는 범위의 소비를 출력해줍니다.