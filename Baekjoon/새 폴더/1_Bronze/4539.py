n = int(input())
# 수의 개수를 받아줍니다.
for _ in range(n):
    number = int(input())
    arr = []
    while True:
        left = number % 10
        arr.append(left)
        number //= 10

        if number == 0:
            break
    # 수를 받아 일의 자리부터 차례대로 리스트에 담아줍니다.

    for i in range(len(arr) - 1):
        if arr[i] >= 5:
            arr[i + 1] += 1
        arr[i] = 0
    # 각 자리를 확인하여 반올림 해줍니다.
    result = arr[-1] * (10 ** (len(arr) - 1))
    # 갱신된 첫자리 수를 가지는 주어진 길이의 수를 구해줍니다.
    print(result)
    # 결과를 출력해줍니다.