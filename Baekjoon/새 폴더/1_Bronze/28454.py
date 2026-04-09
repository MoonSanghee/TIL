today = list(map(int, input().split("-")))
N = int(input())
# 오늘 날짜와 기프트카드의 수를 받아줍니다
result = 0
# 결과를 담을 변수를 설정해줍니다
for _ in range(N):
    gift = list(map(int, input().split("-")))
    # 기프트 카드의 만료일을 받아줍니다
    if gift[0] > today[0]:
        result += 1
    elif gift[0] == today[0]:
        if gift[1] > today[1]:
            result += 1
        elif gift[1] == today[1]:
            if gift[2] >= today[2]:
                result += 1
    # 기프트 카드가 유효한지 확인해줍니다
print(result)
# 결과를 출력해줍니다