t = int(input())
# 테스트케이스의 개수를 받아줍니다
for _ in range(t):
    k = int(input())
    students = list(map(int, input().split()))
    # 수강생의 수와 수강생들의 번호를 받아줍니다
    count = 0
    record = [0, 361]
    # 6시간 이내에 들어온 학생을 담을 변수와 최고기록자와 최고기록을 담을 변수를 설정해줍니다
    n = int(input())
    for _ in range(n):
        number, hours, minutes = map(int, input().split())
        if number not in students:
            continue
        elif hours == -1 or hours > 6:
            continue
        # 수강생이 아니거나 인증서를 못 받았다면 다음을 확인해줍니다
        elif hours * 60 + minutes <= 360:
            count += 1
            if hours * 60 + minutes < record[1]:
                record[0] = number
                record[1] = hours * 60 + minutes
        # 인증서를 받았다면 최고기록자인지 확인하고 각 값을 갱신해줍니다
    print(record[0], count)
    # 결과를 출력해줍니다