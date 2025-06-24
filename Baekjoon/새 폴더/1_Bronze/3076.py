R, C = map(int, input().split())
A, B = map(int, input().split())
# 주지는 변수들을 받아줍니다
result = []
# 전체 체스판의 형태를 담을 변수를 설정해줍니다
for i in range(R):
    line = []
    for j in range(C):
        for _ in range(B):
            if (i + j) % 2 == 0:
                line.append("X")
            else:
                line.append(".")
    for _ in range(A):
        result.append(line)
    # 행열을 각 행별로 들어가는 모양을 전체 체스판에 담아줍니다

for i in result:
    print(''.join(i))
    # 각 행별을 join시켜 출력시켜줍니다