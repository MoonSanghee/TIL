c, h = map(int, input().split())
# 주어지는 상행과 하행 열차의 수를 받아줍니다
result = [1] * (24 * 3600)
# 하루의 매초 차단기가 올라가있다고 설정해줍니다
for _ in range(c + h):
    h, m, s = map(int, input().split(':'))
    s += m * 60 + h * 3600
    # 열차가 지나가는 시간을 받아 초로 환산해줍니다
    for i in range(40):
        result[s + i] = 0
    # 차단기가 내려가는 시간을 갱신해줍니다

print(sum(result))
# 차단기가 올라가있는 시간의 합을 출력해줍니다