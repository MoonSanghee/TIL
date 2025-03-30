N, r, c = map(int, input().split())
result = 0
# 주어지는 영역의 크기와 위치를 받아줍니다
while N != 0:
    N -= 1
    if r < 2 ** N and c < 2 ** N:
        result += (2 ** N) * (2 ** N) * 0
    elif r < 2 ** N and c >= 2 ** N:
        result += (2 ** N) * (2 ** N) * 1
        c -= (2 ** N)
    elif r >= 2 ** N and c < 2 ** N:
        result += (2 ** N) * (2 ** N) * 2
        r -= (2 ** N)
    else:
        result += (2 ** N) * (2 ** N) * 3
        r -= (2 ** N)
        c -= (2 ** N)
    # 영역을 4등분하여 각 영역에서 어느 4분면에 위치하는지 확인하여 체워지는 칸만큼 값을 더하여 4분할이 되지않을때까지 진행합니다
print(result)
# 결과값을 출력해줍니다