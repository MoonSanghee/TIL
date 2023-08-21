n, w, h = map(int, input().split())
# 성냥의 개수와 너비 높이를 받아줍니다.
c = w ** 2 + h ** 2
# 대각의 길이를 구해줍니다.
for _ in range(n):
    num = int(input())
    # 성냥의 길이를 받아줍니다.
    if num ** 2 > c:
        print('NE')
    else:
        print('DA')
    # 성냥이 대각선의 길이보다 긴지 확인하고 맞는 값을 출력해줍니다.