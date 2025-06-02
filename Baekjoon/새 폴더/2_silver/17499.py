n, q = map(int, input().split())
arr = list(map(int, input().split()))
move = 0
# 주어지는 배열의 크기와 연산의 크기, 수열을 받아줍니다
# 얼마나 움직일지를 담을 변수를 받아줍니다
for _ in range(q):
    command = list(map(int, input().split()))
    if command[0] == 1:
        arr[(move + command[1] - 1) % n] += command[2]
        # 움직인 상태를 확인하여 바뀌는 위치에 연산을 실행해줍니다
    elif command[0] == 2:
        move -= command[1]
    else:
        move += command[1]
    # 움직이는 방향에 따라 주어진 값만큼 더하거나 빼줍니다
for i in range(n):
    print(arr[(i + move) % n], end = ' ')
# 움직임을 적용하여 배열의 값을 차례대로 출력해줍니다