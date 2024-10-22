n = int(input())
# 카드의 장수를 받아줍니다
d = dict()

for _ in range(n):
    s, x = input().split()
    d[s] = d.get(s, 0 ) + int(x)
    # 각 문양이 몇개씩 나와있는지 받아줍니다.
for i in d:
    if d[i] == 5:
        print("YES")
        break
else:
    print("NO")
    # 결과를 출력해줍니다.