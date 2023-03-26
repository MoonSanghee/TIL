numbers = list(map(int, input().split()))
n = min(numbers)
# 숫자 5개를 입력받고 가장 작은 수를 찾아줍니다.
while True:
    cnt = 0
    for i in range(5):
        if n % numbers[i] == 0:
            cnt += 1
        # 숫자들을 순회하며 n에 저장한 수로 나누어 떨어지는 숫자의 개수를 확인해줍니다,
    if cnt > 2:
        print(n)
        break
    # 나누어 떨어지는 수가 3개 이상이라면 원하는 값을 찾았으니 출력해주고
    n += 1
    # 아니라면 n에 1울 더하여 반복해줍니다.