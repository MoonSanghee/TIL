a, b, c = map(int, input().split())
# 3개의 주사위가 몇개의 면을 가지고있는지 받습니다.
com = dict()
for i in range(a):
    for j in range(b):
        for k in range(c):
            num = i + j + k + 3
            if num in com:
                com[num] += 1
            else:
                com[num] = 1
# 나올수 있는 조합의 합을 세어 줍니다.
number = 0
cnt = 0
for i in com:
    if com[i] > cnt:
        number = i
        cnt = com[i]
# 조합의 합이 더 자주 나오면 값을 갱신해줍니다.
print(number)
# 가장 많이 나오는 합 값을 출력해줍니다.