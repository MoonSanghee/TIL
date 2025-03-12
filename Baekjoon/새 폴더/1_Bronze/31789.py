n = int(input())
x, s = map(int, input().split())
flag = False
# 주어지는 무기의 개수와 가진 돈, 후안의 공격력을 받아줍니다
for _ in range(n):
    c, p = map(int, input().split())
    if c <= x and p > s:flag = True
    # 주어지는 무기를 살 수 있고 공격력이 후안보다 강하다면 모험을 떠날 수 있다고 갱신해줍니다
if flag:print("YES")
else:print("NO")
# 모험을 떠날 수 있는지를 출력해줍니다