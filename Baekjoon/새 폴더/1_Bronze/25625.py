x, y = map(int, input().split())
# 주어지는 두 정수를 받아줍니다
if x < y:
    print(y - x)
# y가 x보다 크다면 버스가 서울대입구역으로 오고있으므로 y-x를
else:
    print(x + y)
# 아니라면 둘을 더한 값을 출력해줍니다