n = int(input())
numbers = list(map(int, input().split()))
# 주어지는 수열의 길이와 수열을 받아줍니다
arr = [[0] * 21 for _ in range(n - 1)]
# n길이의 만들어질수 있는 경우의 수를 담을 리스트를 만들어줍니다
arr[0][numbers[0]] = 1
# 음수를 모르므로 첫 수는 더할수밖에 없습니다
for i in range(1, n - 1):
    for j in range(21):
        if arr[i - 1][j] != 0:
            # 이전 단계에서 만들어질수 있는 수를 찾아줍니다
            if j - numbers[i] >= 0:
                arr[i][j - numbers[i]] += arr[i - 1][j]
            if j + numbers[i] <= 20:
                arr[i][j + numbers[i]] += arr[i - 1][j]
            # 이전 단계의 수에서 더하거나 빼서 범위를 벗어나는지 확인해줍니다
print(arr[-1][numbers[-1]])
# 목표값을 만드는 방법의 수를 출력해줍니다