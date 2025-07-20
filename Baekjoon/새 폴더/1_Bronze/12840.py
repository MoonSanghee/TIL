h, m, s = map(int, input().split())
seconds = 3600 * h + 60 * m + s
# 최초의 시간을 받아 초로 변화하여줍니다
n = int(input())
# 주어지는 입력의 개수를 받아줍니다
for _ in range(n):
    command = list(map(int, input().split()))
    # 주어지는 명령어를 받아줍니다
    if command[0] == 1:
        seconds += command[1]
        seconds %= (24 * 3600)
    elif command[0] == 2:
        seconds -= command[1]
        seconds %= (24 * 3600)
    elif command[0] == 3:
        h = seconds // 3600 
        m = (seconds % 3600) // 60
        s = seconds % 60
        print(h, m, s)
        # 주어지는 명령어가 1이나 2라면 값을 수정해주고 3이라면 현재 초를 시간으로 변환하여 출력해줍니다