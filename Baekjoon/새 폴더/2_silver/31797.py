n, m = map(int, input().split())
n %= (m * 2)
# 층수와 참가하는 사람의 수를 받아줍니다.
# 온전히 손이 다 돌고 몇번째 남은 손을 확인해야하는지 구해줍니다
hands = []
d = dict()
# 손의 위치를 담고 손이 누구의 손인지 담을 리스트와 딕셔너리를 만들어줍니다.
for i in range(1, m + 1):
    l, r = map(int, input().split())
    hands.append(l)
    hands.append(r)
    d[l] = i
    d[r] = i
    # 양 손의 높이를 리스트에 넣고 딕셔너리에 누구의 손이 어느 높이에 있는지 받아줍니다.

hands.sort()
# 손을 높이에 따라 정렬시켜줍니다.
print(d[hands[n - 1]])
# 당첨된 사람을 출력해줍니다.