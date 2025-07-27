maps = [list(input().split()) for _ in range(10)]
flag = False
# 전체 영역의 상태와 한 두름을 만들수 있는지를 담을 변수를 설정해줍니다
for i in range(10):
    c = set()
    r = set(maps[i])
    for j in range(10):
        c.add(maps[j][i])
    if len(c) == 1 or len(r) == 1:
        flag = True
# 행과 열을 확인하여 한 두름을 만들수 있는지 확인해줍니다
if flag:
    print(1)
else:
    print(0)
    # 결과를 출력해줍니다