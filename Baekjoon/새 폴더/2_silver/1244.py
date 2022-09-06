def change(n):
    if switch[n] == 0:
        switch[n] = 1
    else:
        switch[n] = 0
    return

N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num, N + 1, num):
            change(i)
    else:
        change(num)
        for j in range(N//2):
            if num + j <= N and num - j >= 1:
                if switch[num + j] == switch[num - j]:
                    change(num + j)
                    change(num - j)
                else:
                    break

for i in range(1, N + 1):
    print(switch[i], end = ' ')
    if i % 20 == 0:
        print()