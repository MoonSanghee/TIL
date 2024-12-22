n = int(input())
# n을 받아줍니다
cnt = (n * 2 + 1) ** 2
# a가 0일떄 모든 조합에 대하여 식이 성립하므로 n이 0일때 만들수 있는 조합의 수를 결과값에 담아줍니다
for a in range(-n, n + 1, 1):
    if a == 0:
        continue
    # a가 0인 모든 경우를 이미 결과값에 적용하였으므로 a가 0인 경우는 continue해줍니다.
    for b in range(-n, n + 1, 1):
        if abs(1 - a - b) <= n:
            cnt += 1
            # b를 순회하며 식이 유효하다면 c가 존재하므로 cnt 값을 갱신해줍니다

print(cnt)
# 결과값을 출력해줍니다.