t = int(input())
hands = 'RSP'
# 테스트 케이스와 가위, 바위, 보를 받아줍니다
for _ in range(t):
    n = int(input())
    result = 0
    # 가위, 바위, 보를 한 횟수와 결과를 담을 변수를 받아줍니다.
    for _ in range(n):
        p1, p2 = input().split()
        if p1 == hands[hands.index(p2) - 1]:
            result += 1
        elif p2 == hands[hands.index(p1) - 1]:
            result -= 1
    # 승자를 표시해줍니다.
    if result > 0:
        print("Player 1")
    elif result == 0:
        print("TIE")
    else:
        print("Player 2")
    # 결과를 출력해줍니다.