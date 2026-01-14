x, y = map(int, input().split())
if x < y:
    x, y = y, x
# 주어지는 두 수를 받아줍니다
for i in range(x):
    if i < x - y:
        print('1', end='')
    else:
        print('2', end='')
print()
# 결과를 출력하여줍니다