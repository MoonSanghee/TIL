d1, d2, d3 = map(int, input().split())
# 세 정수를 받아줍니다
a = (d1 + d2 - d3) / 2
b = d1 - a
c = d2 - a
# 주어진 세 정수로 a, b, c값을 찾아줍니다
if a > 0 and b > 0 and c > 0:
    print(1)
    print("%.1f %.1f %.1f" %(a, b, c))
    # 조건이 유효한지 확인해 유효하다면 주어진 양식에 맞게 출력해주고
else:
    print(-1)
    # 유효하지 않다면 -1을 출력해줍니다