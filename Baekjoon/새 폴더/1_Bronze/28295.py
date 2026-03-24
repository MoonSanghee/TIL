result = 0
# 지시로 이동한 결과를 담을 변수를 설정해줍니다
for _ in range(10):
    result += int(input())
# 지시에 따라 이동을 실행해줍니다
result %= 4
# 4방향이므로 4로 나눈 나머지를 구해줍니다
if result == 0:
    print("N")
elif result == 1:
    print("E")
elif result == 2:
    print("S")
else:
    print("W")
# 바라보는 방향을 출력해줍니다