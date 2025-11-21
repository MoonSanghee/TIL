n = int(input())
numbers = list(map(int, input().split()))
# 주어지는 수열의 길이와 수열을 받아줍니다
result = [1, 0]
length = 1
# 결과를 담을 변수와 현재 길이를 담을 변수를 설정해줍니다
for i in range(1, n):
    if numbers[i] < numbers[i - 1]:
        result[0] += 1
        result[1] = max(result[1], length)
        length = 1
    else:
        length += 1
    # 수열이 이어지는지 확인하여 새로 시작해야한다면 수열의 개수를 갱신하고 최장 수열의 길이를 확인한 후 수열을 초기화 시켜줍니다
result[1] = max(result[1], length)
# 마지막 수열의 길이를 비교해줍니다
print(*result)
# 결과를 주어진 형식에 맞게 출력하여줍니다