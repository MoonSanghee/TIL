n, m = map(int, input().split())
flogs = [list(map(int ,input().split())) for _ in range(n)]
# 연꽃과 통나무의 개수를 받고 개구리의 대화 흥미도를 받아줍니다.
for i in range(n):
    favorite = list(map(int, input().split()))
    flogs[i] += favorite
    # 개구리가 앉을수 있는 연꽃의 위치를 받아줍니다.

legs = [list(map(int, input().split())) for _ in range(m)]
# 통나무의 정보에 대해 받아줍니다.
flowers = [0] * (n + 1)
happy = False
result = [0] * n
# 연꽃에 앉은 상태와 대화가 잘 이루어지는지 대화가 잘 이루어 진다면 어떤 식으로 개구리를 배치할 수 있는지 담을 변수를 설정해줍니다.

def position(i):
    global happy, result
    if i != n:
        # 개구리를 배치하는 함수입니다.
        # 개구리가 아직 남았다면 개구리를 앉을수 있는 연꽃이 비었는지 확인하고 모든 개구리를 배치하여줍니다.
        if flowers[flogs[i][4]] == 0:
            flowers[flogs[i][4]] = i + 1
            position(i + 1)
            flowers[flogs[i][4]] = 0
        if flowers[flogs[i][5]] == 0:
            flowers[flogs[i][5]] = i + 1
            position(i + 1)
            flowers[flogs[i][5]] = 0
    else:
        # 개구리를 모두 배치하였다면
        # 통나무의 대화 주세를 확인하여 모든 개구리가 정해진 주제로 대화를 확인해줍니다.
        for a, b, sub in legs:
            if flogs[flowers[a] - 1][sub - 1] != flogs[flowers[b] - 1][sub - 1]:
                break
        else:
            happy = True
            result = flowers[1:]
            # 모두 대화가 이루어진다면 대화가 이루어 진다고 수정하고 reuslt에 개구리의 배치를 담아줍니다.
        return

position(0)
# 0번 인덱스의 개구리부터 배치를 시작합니다.
if not happy:
    print("NO")
else:
    print("YES")
    print(*result)
    # 모든 개구리가 대화할 수 있는지 확인하고 결과를 출력해줍니다.