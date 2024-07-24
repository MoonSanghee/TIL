t = int(input())
# 입력되는 테스트 케이스의 수를 받아줍니다.
for _ in range(t):
    x, y = map(int, input().split())
    # x, y 값을 받아줍니다.
    if 0 <= x <= 23 and 0 <= y <= 59:
        time = 'Yes'
    else:
        time = 'No'
    # 시간으로 출력가능한지 확인하고 출력할 값을 변수에 담아줍니다.
    if 1 <= x <= 12:
        if x == 2 and 1 <= y <= 29:
            date = "Yes"
        elif x in [1, 3, 5, 7, 8, 10, 12] and 1 <= y <= 31:
            date = "Yes"
        elif 1 <= y <= 30:
            date = "Yes"
        else:
            date = "No"
    else:
        date = "No"
    # 날짜로 출력 가능한지 확인하고 변수에 출력할 값을 담아줍니다.
    print(f'{time} {date}')
    # 시간과 날짜로 출력 가능한지 형식에 맞게 출력해줍니다.