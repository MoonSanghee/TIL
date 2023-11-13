tc = int(input())
# 시행횟수를 받아줍니다.
for t in range(tc):
    blank = input()
    # 학생수를 받기전에 여백이 입력됩니다.
    n = int(input())
    # 학생수를 받아줍니다.
    total = 0
    # 전체 사탕수를 담을 변수를 만들어줍니다.
    for _ in range(n):
        total += int(input())
    # 각 학생들의 사탕수를 더해줍니다.
    if total % n == 0:
        print('YES')
    else:
        print('NO')
    # 똑같이 나눌수 있는지 여부를 출력해줍니다.