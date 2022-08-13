test = int(input())
for t in range(test):
    numbers = [1, 1, 1, 2, 2]
    n = int(input())
    if n > 4:
        for i in range(n - 5):
            numbers.append(numbers[i] + numbers[i + 4])
    print(numbers[n - 1])
    # [1, 1, 1, 2 ,2]를 기준으로 다음 값의 위치를 n이라고하면 n은 n - 1과 n - 5 위치의 값의 합이다.