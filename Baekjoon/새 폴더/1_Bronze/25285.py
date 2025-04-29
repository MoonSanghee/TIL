t = int(input())
# 테스트케이스의 수를 받아줍니다
for _ in range(t):
    cm, kg = map(int, input().split())
    m = cm / 100
    bmi = kg / (m ** 2)
    # 주어지는 신장과 몸무게를 받아 bmi값을 구해줍니다
    if 161 <= cm < 204:
        if 20 <= bmi < 25:
            print(1)
        elif 18.5 <= bmi < 30:
            print(2)
        elif 16 <= bmi < 35:
            print(3)
        else:
            print(4)
    elif 159 <= cm < 161:
        if 16 <= bmi < 35:
            print(3)
        else:
            print(4)
    elif cm >= 146:
        print(4)
    elif cm >= 140.1:
        print(5)
    else:
        print(6)
    # 주어진 조건에서 신체등급을 찾아 출력해줍니다