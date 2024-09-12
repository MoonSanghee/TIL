n = int(input())

d = dict()
cnt = 0

for _ in range(n):
    pizza = input()
    d[pizza] =  d.get(pizza, 0) + 1
# 친구들이 먹는 피자조각의 크기를 받아줍니다.
if d.get('3/4', 0) >= d.get('1/4', 0):
    half = d.get('1/2', 0)
    cnt = d.get('3/4', 0) + half // 2 + half % 2
    # '3/4'크기 조각을 먹는 친구가 '1/4' 크기를 먹는 친구와 같거나 많다면
    # '3/4'을 먹는 친구수와 반판을 먹는 친구를 위해 필요한 피자를 더해 답을 구합니다.
else:
    # '1/4'판을 먹는 친구가 더 많다면 
    half = d.get('1/2', 0)
    quarter = d.get('1/4', 0)
    
    cnt += d.get('3/4', 0) + half // 2

    quarter -= d.get('3/4', 0)
    cnt += quarter // 4
    # 온전한 한판을 사용하는 경우를 다 더하고
    if quarter % 4 + (half % 2) * 2 >= 4:
        cnt += 2
    elif quarter % 4 + (half % 2) * 2 > 0:
        cnt += 1
    # 자투리가 몇 판 필요한지 확인해줍니다.

print(cnt)
# 답을 출력해줍니다.