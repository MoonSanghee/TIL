t, s = map(int, input().split())
# 시간과 음주여부를 받아줍니다.
if t in range(12, 17) and s == 0:
    print(320)
else:
    print(280)
    # 조건을 확인하여 밥알의 수를 출력해줍니다.