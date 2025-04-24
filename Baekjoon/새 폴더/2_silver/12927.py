lamps = ['N'] +list(input())
cnt = 0
# 인덱스 위치를 버튼 위치와 맞춰주기위해 0번 인덱스에 N상태의 전구를 더하고 주어지는 상태를 받아줍니다
# 버튼을 작동시키는 횟수를 담을 변수를 설정해줍니다
for i in range(1, len(lamps)):
    if lamps[i] == 'Y':
        for j in range(i, len(lamps), i):
            if lamps[j] == 'Y':
                lamps[j] = 'N'
            else:
                lamps[j] = 'Y'
        cnt += 1
# 각 인덱스 자리의 전구가 켜져있다면 스위치를 작동시키고 배수의 전구를 키거나 꺼줍니다
print(cnt)
# 스위치를 작동시킨 횟수를 출력해줍니다