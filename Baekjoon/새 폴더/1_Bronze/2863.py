a, b = map(int, input().split())
c, d = map(int, input().split())
# 네 수를 받아줍니다.
com = [a/c + b/d, c/d + a/b, d/b + c/a, b/a + d/c]
# 수를 돌려 나오는 계산 값을 구해줍니다.
p = 0
num = com[0]
# 돌리지 않았을 때의 값을 기본으로 설정해줍니다.
for i in range(4):
    if com[i] > num:
        num = com[i]
        p = i
    # 차례대로 돌렸을때 값이 크면 몇 번 돌렸을 경우인지 표시해줍니다.
print(p)
# p의 값을 출력해줍니다.