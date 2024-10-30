p = int(input())
# 학생의 수를 받아줍니다
result = [0, 0, 0, 0]
# 각 과의 학생수를 담을 변수를 설정해줍니다
for _ in range(p):
    g, c, n = map(int, input().split())

    if g == 1:
        result[3] += 1
        # 1학년이라면 과에 속하지 않습니다.
    else:
        if c == 1 or c == 2:
            result[0] += 1
        elif c == 3:
            result[1] += 1
        else:
            result[2] += 1
        # 반을 확인하여 각 과의 학생으로 추가해줍니다.

for i in result:
    print(i)
    # 요청받을 순서대로 출력해줍니다