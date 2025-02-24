n = int(input())
cnt = 0
# 주어지는 범위와 당첨 복권의 수를 담을 변수를 설정해줍니다
for i in range(2023, n + 1):
    number = str(i)
    check = 0
    for j in '023':
        if j not in number:
            break
    # 2023 미만은 당첨 복권이 없으므로 2023 이상의 복권에서 0, 2, 3을 포함한 수를 걸러줍니다 
    else:
        for j in number:
            if j == '2023'[check]:
                check += 1
                if check == 4:
                    break
    if check == 4:
        cnt += 1
    # 거른 수가 당첨 번호를 가지고있는지 확인해줍니다
print(cnt)
# 당첨 복권의 수를 출력해줍니다