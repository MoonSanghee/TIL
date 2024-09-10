n, m, k = map(int, input().split())
# 극장의 크기와 동아리원의 수를 받아줍니다.
theater = [input() for _ in range(n)]
# 극장의 예매 상태를 받아줍니다.
count = 0
# 경우의수를 담을 변수를 설정해줍니다.
for i in range(n):
    straight = 0
    for j in range(m):
        if theater[i][j] == '0':
            straight += 1
            if straight >= k:
                count += 1
        else:
            straight = 0
        # 연속한 빈자리를 확인하고 동아리원수 이상이라면 경우의수를 갱신해줍니다.
        
print(count)
# 결과를 출력해줍니다.