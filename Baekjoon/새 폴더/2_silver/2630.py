n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
# n * n 의 종이를 받아줍니다.
bw = [0, 0]
# 흰색과 파란색을 기록할 리스트를 만들어 줍니다.
def check(x, y, z):
    a = maps[x][y]
    z2 = z//2
    for i in range(x, x + z):
        for j in range(y, y + z):
            # x와 y부터 z의 크기만큼이 모두 일치하는지 확인해줍니다.
            if maps[i][j] != a:
                check(x, y, z2)
                check(x + z2, y, z2)
                check(x, y + z2, z2)
                check(x + z2, y + z2, z2)
                return
                # 다른갑이 존재한다면 4분할하여 확일할 때 z의 반만큼 그 자리와 x만큼 떨어진 자리
                # y만큼 떨어진 자리, x와 y 모두 떨어진 자리 4군데를 확인하여주고 아무값도 변경시키지 않습니다.
    if a == 1:
        bw[0] += 1
    else:
        bw[1] += 1
        # 리턴되지않고 모두 동일한 값을 가지고 있다면 bw리스트에 어떠한 값인지 저장하여줍니다.

check(0, 0, n)
# 0,0에서 n의 크기부터 작아지기때문에 최대인 n으로 작동시켜주고
print(bw[1])
print(bw[0])
# bw 리스트에 넣어준 하얀색과 파란색 종이의 수를 차례대로 출력해줍니다.


# 문제가 안 풀릴때 보고만 있으면 아무런 아이디어도 떠오를리 없다.
# 뭐라도 쓰고 틀려보는것이 만배낫다!!!