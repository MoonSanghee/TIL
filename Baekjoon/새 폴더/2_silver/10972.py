n = int(input())
perm = list(map(int, input().split()))
# 수의 개수와 기준 수열을 받아줍니다

for i in range(n - 1, 0, -1):
    if perm[i - 1] < perm[i]:
        # 뒤의 값보다 앞의 값보다 큰 값이 있는지 확인하고
        for j in range(n - 1, 0, -1):
            # 뒤집을수 있는 영역이 있는지 확인해줍니다
            if perm[i - 1] < perm[j]:
                perm[i - 1], perm[j] = perm[j], perm[i - 1]
                perm = perm[:i] + sorted(perm[i:])
                print(" ".join(map(str, perm)))
                exit()
            # 영역이 존재하면 뒤집어 다음 수열을 만들어 출력하고 확인을 멈추어줍니다.
print(-1)
# 멈추지 않았다면 -1을 출력해줍니다.