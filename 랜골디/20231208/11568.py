n = int(input())
numbers = list(map(int, input().split()))
# 수의 개수와 수열을 받아줍니다.
check = [0] * n

for i in range(n):
    for j in range(i + 1, n):
        if numbers[j] > numbers[i]:
            check[j] = max(check[i] + 1, check[j])
        # 각 자리 수의 다음 자리부터 본인 보다 큰 수를 비교하여 본인을 통해 도달하는 경우가 더 길다면 값을 갱신하여줍니다.

print(max(check) + 1)
# check리스트의 최대값에 1을 더하여 출력해줍니다.