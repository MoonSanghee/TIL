n = int(input())
arr = []
for i in range(n):
    arr.append(i * 2 + 1)
print(*arr)
# 수열을 이루는 모든 수가 홀수라면 두 수의 합인 짝수는 두 수를 곱한 수의 약수가 될수 없습니다.