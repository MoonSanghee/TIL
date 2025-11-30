time = list(input().split())
n, t = map(int, input().split())
# 주어지는 변수들을 받아줍니다
time[0] = int(time[0][:2]) * 60 + int(time[0][3:])
time[1] = int(time[1][:2]) * 60 + int(time[1][3:])
# 시간에 60을 곱해 분단위로 바꾸어줍니다
cnt = 0
days = 0
result = time[0]
# 배달한 택배와 지난 날의수 배송이 완료된 시간을 담을 변수를 설정해줍니다
while cnt <= n:
    if result + t < time[1]:
        result += t
    # 배송을 했을때 퇴근 시간이 넘지 않는 경우에만 그 날 배송을 진행합니다
    else:
        days += 1
        result = time[0] + t
    # 퇴근시간이 되거나 퇴근시간이 지나야 배송할 수 있다면 다음날 배송을 합니다
    cnt += 1
    # 배송한 택배의 수를 갱신해줍니다

print(days)
print(f'{result // 60:02d}:{result%60:02d}')
# 걸리는 날과 예측 배송완료시간을 주어진 형식에 맞게 출력해줍니다