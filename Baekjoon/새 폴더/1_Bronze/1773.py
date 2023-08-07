n, c = map(int, input().split())
li = [0] * (c + 1)
# 폭죽의 종류와 제한 시간을 받아줍니다.
for _ in range(n):
    t = int(input())
    # 폭죽의 주기를 받아줍니다.
    if t == 1:
        print(c)
        quit()
        # 주기가 1초라면 c를 출력합니다.
    for i in range(t, c + 1, t):
        li[i] = 1
        # 아니라면 폭죽이 터지는것을 표시해줍니다.

print(sum(li))
# 주기가 1이 아니어서 계속 진행되었다면 li의 합을 출력해줍니다.