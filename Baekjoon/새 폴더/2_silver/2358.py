n = int(input())
# 좌표의 개수를 받아줍니다.
dx = dict()
dy = dict()
answer = 0
# 좌표가 선이 되는지 담을 dx, dy 딕셔너리를 만들어줍니다.
for i in range(n):
    x, y = map(int, input().split())
    if x in dx:
        dx[x] = True
    else:
        dx[x] = False
    if y in dy:
        dy[y] = True
    else:
        dy[y] = False
    # x, y 좌표를 받고 직선이 되는지 확인하여 딕셔너리의 value를 설정해줍니다.
    
for v in dx.values():
    if v:
        answer += 1

for v in dy.values():
    if v:
        answer += 1

print(answer)
# 딕셔너리를 순회하여 직선이 되는 값의 수를 확인해 출력해줍니다.