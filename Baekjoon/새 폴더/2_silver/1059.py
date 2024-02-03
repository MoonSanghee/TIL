n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
# 숫자의 개수와 수열을 입력받고 정렬을 실행시켜줍니다.
check = int(input())
# 좋은 구간에 포함되는지 확인할 수를 받아줍니다.

if check in numbers:
    print(0)
    # check가 수열에 포함된다면 좋은 구간이 존재하지 않습니다.
else:
    cnt = 0
    start = 0
    for number in numbers:
        if number < check:
            start = number
        elif number > check:
            end = number
            break
    # 수열의 연속한 두 수가 확인할 수를 포함하는 구간을 찾아줍니다.

    for i in range(start + 1, end - 1):
        for j in range(i + 1, end):
            if check in range(i, j + 1):
                cnt += 1
    # 좋은 구간을 찾아줍니다.
    
    print(cnt)
    # 좋은 구간의 수를 출력해줍니다.