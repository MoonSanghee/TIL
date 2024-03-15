li = []
cnt = 0
# 수를 담을 리스트와 수가 존재하는지 확인할 변수를 설정합니다.
while True:
    try:
        # 입력이 유효한지 확인해줍니다.
        nubmers = input().split()
        for i in nubmers:
            if cnt != 0:
                i = ''.join(reversed(i))
                li.append(int(i))
            cnt += 1
        # 입력 받은 수들을 나누고 각 수를 뒤집어 리스트에 넣어줍니다.
    except:
        break
    # 입력이 유효하지 않다면 리스트에 담는것을 멈추어줍니다.

result = sorted(li)
# 리스트를 오름차순으로 정렬해줍니다.
for i in result:
    print(i)
    # 리스트에 든 수를 차례대로 출력해줍니다.