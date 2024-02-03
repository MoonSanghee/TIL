n, m = map(int, input().split())
drops = int(input())
# 스크린 크기와 바구니 크기, 떨어지는 사과의 개수를 받아줍니다.
s = 1
e = m
move = 0
# 바구니는 가장 왼 쪽에 붙도록 위치하므로 s를 1 e를 m으로 설정하고
# 이동거리를 0으로 설정해줍니다.

for _ in range(drops):
    apple = int(input())
    # 사과가 떨어질 위치를 받아줍니다.
    if apple < s:
        move += s - apple
        s = apple
        e = apple + m - 1
        # 바구니가 스크린을 넘을 수 없으므로 사과가 바구니보다 앞에 떨어진다면 왼쪽으로
    elif apple > e:
        move += apple - e
        e = apple
        s = e - m + 1
        # 아니라면 오른쪽으로 이동시키도 이동해야하는 거리를 확인해줍니다.

print(move)
# 이동해야하는 거리를 출력해줍니다.