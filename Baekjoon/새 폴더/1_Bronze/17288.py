number = input()
# 주어진 수를 받아줍니다.
cnt = 0
# 3개 연속한 수의 개수를 담을 변수를 설정해줍니다.
idx = 0
straight = 0
# 확인한 인덱스 자리와 연속한 길이를 담을 변수를 확인해줍니다.
while True:
    if idx == len(number) - 1:
        break
    # 모든 수를 확인했다면 반복을 멈추어줍니다.
    num = int(number[idx])
    straight = 1
    # 자리의 시작 수를 받고 1길이만큼 연속함을 표시해줍니다.
    for i in range(idx + 1, len(number)):
        idx = i
        if int(number[i]) == num + 1:
            num = int(number[i])
            straight += 1
        else:
            break
        # idx다음부터 연속한 수인지 확인해주고 연속이 끝날때까지 남은 범위를 확인해줍니다.
    if straight == 3:
        cnt += 1
        # 3만큼 연속한다면 연속하는 수의 개수를 1추가해줍니다.

print(cnt)
# cnt에 담긴 3연속하는 수의 개수를 출력해줍니다.