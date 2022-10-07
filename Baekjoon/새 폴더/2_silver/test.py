seet = []
for i in range(5):
    seet.append(list(map(int, input().split())))

check = [[0 for _ in range(5)] for _ in range(5)]

called = []
for i in range(5):
    nums = list(map(int, input().split()))
    for j in range(5):
        called.append(nums[j])

for i in range(25):
    for j in range(5):
        for k in range(5):
            if seet[j][k] == called[i]:
                check[j][k] = i + 1

num = 26

def bingo(x, y):
    global num
    cnt = 0
    for i in range(5):
        for j in range(5):
            if check[i][j] > check[x][y]:
                break
        else:
            cnt += 1
    for i in range(5):
        for j in range(5):
            if check[j][i] > check[x][y]:
                break
        else:
            cnt += 1
    for i in range(5):
        if check[i][i] > check[x][y]:
            break
    else:
        cnt += 1

    for i in range(5):
        if check[i][4 - i] > check[x][y]:
            break
    else:
        cnt += 1
    if cnt > 2 and num > check[x][y]:
        num = check[x][y]
print(num)