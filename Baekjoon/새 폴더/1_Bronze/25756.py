n = int(input())
As = list(map(int, input().split()))
# 주어지는 물약과 효과를 받아줍니다
result = 0

for i in As:
    now = 1 - (result / 100)
    will_cut = 1 - (i / 100)
    result = (1 - (now * will_cut)) * 100
    print(result)
    # 주어지는 효과를 차례대로 적용한 결과를 출력해줍니다