n = int(input())
arr =list(map(int, input().split()))
# 주어지는 수열의 길이와 수열을 받아줍니다
numbers = [0] * 11
# 값의 범위가 10 이하의 자연수이므로 이렇게 설정해줍니다
left = 0
result = 0
# 수열의 시작인덱스와 최장 길이를 담을 변수를 설정해줍니다
for right in range(n):
    numbers[arr[right]] += 1

    while True:
        minimum = next(i for i in range(11) if numbers[i] > 0)
        maximum = next(i for i in range(10, -1, -1) if numbers[i] > 0)
        # 현재 주어진 범위의 최소값과 최대값을 확인해줍니다
        if maximum - minimum <= 2:
            break
        # 수열의 범위가 유효하다면 반복을 멈추어줍니다

        numbers[arr[left]] -= 1
        left += 1
        # 수열이 유효하지않다면 왼쪽부터 한 칸씩 당겨줍니다

    result = max(result, right - left + 1)
    # 수열의 최장 길이를 비교하여 갱신해줍니다
print(result)
# 결과를 출력해줍니다