n = int(input())
trees = list(map(int, input().split()))
# 나무의 수와 나열된 나무의 상태를 받아줍니다
result = 0
# 최종 결과를 담을 변수를 설정해줍니다

# 나무가 최대 10그루이므로 4번의 반복을 통해 모든 그룹을 설정하였을때 값을 구해 비교해줍니다
I = 1
for i in range(n - 3):
    I *= trees[i]
    J = 1
    for j in range(i + 1, n - 2):
        J *= trees[j]
        K = 1
        for k in range(j + 1, n - 1):
            K *= trees[k]
            L = 1
            for l in range(k + 1, n):
                L *= trees[l]
                result = max(result, I + J + K + L)

print(result)
# 결과를 출력해줍니다