t = int(input())
for test in range(1, t + 1):
    num = list(map(int, input().split()))
    new = []
    for i in range(7):
        for j in range(i + 1, 7):
            for k in range(j + 1, 7):
                new.append(num[i] + num[j] + num[k])
    new = sorted(list(set(new)))
    print(f'#{test} {new[-5]}')