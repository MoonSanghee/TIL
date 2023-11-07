n, x = map(int, input().split())
numbers = list(map(int, input().split()))
# n, x일과 n일동안 방문한 사람을 받아줍니다.
if max(numbers) == 0:
    print("SAD")
    # n일동안 하루 최대 방문자가 0명이라면 아무도 방문한적이 없는것이므로
    # "SAD"를 출력해줍니다.
else:
    maximum = sum(numbers[:x])
    value = maximum
    cnt = 1
    # 첫 x일동안 방문자를 확인하여 maximum에 담아주고 maximum과 비교할 value를 만들어줍니다.
    # maximum만큼 방문한 날의 수를 1로 설정해줍니다
    
    for i in range(x, n):
        value -= numbers[i - x]
        value += numbers[i]
        if value > maximum:
            maximum = value
            cnt = 1
        elif value == maximum:
            cnt += 1
    # x일 이후 방문객을 비교하여 최대 방문자가 갱신된다면 cnt값도 갱신해주고
    # 동일한 최대 방문자를 기록하면 cnt값을 1 더해줍니다.
    print(maximum)
    print(cnt)
    # maximum값과 cnt 값을 차례대로 출력해줍니다.