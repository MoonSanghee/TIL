now = list(map(int, input().split(':')))
target = list(map(int, input().split(':')))
# 현재 시간과 목표 시간을 받아줍니다
N = now[0] * 3600 + now[1] * 60 + now[2]
T = target[0] * 3600 + target[1] * 60 + target[2]
# 두 시간을 초로 변환해줍니다.
if T <= N:
    T += 24 * 3600
R = T - N
# 1초 이상 24시간 이하의 시간이 필요하므로 계산 결과가 그 밖이라면 24시간을 더해줍니다.
answer = f'{str(R // 3600).zfill(2)}:{str((R % 3600) // 60).zfill(2)}:{str(R % 60).zfill(2)}'
print(answer)
# 주어진 형식에 맞추어 출력해줍니다.