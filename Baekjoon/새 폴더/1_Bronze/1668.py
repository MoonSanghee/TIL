n = int(input())
trophies = [int(input()) for _ in range(n)]
left_cnt = right_cnt = 0
left_max = right_max = 0
for trophy in trophies:
    if trophy > left_max:
        left_max = trophy
        left_cnt += 1
for trophy in trophies[::-1]:
    if trophy > right_max:
        right_max = trophy
        right_cnt += 1
print(left_cnt)
print(right_cnt)