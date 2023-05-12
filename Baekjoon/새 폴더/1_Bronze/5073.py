while True:
    nums = sorted(list(map(int, input().split())))
    # 세 수를 리스트로 받아 정렬하여줍니다.
    s = set(nums)
    if len(s) == 1 and 0 in s:
        break
    # 모든 값이 0이면 멈추어줍니다.
    if len(s) == 1:
        print('Equilateral')
    # 모든 값이 같고 0이 아니면 정삼각형입니다.
    elif nums[0] + nums[1] <= nums[2]:
        print('Invalid')
    # 가장 긴 변의 길이가 나머지 두 변의 길이보다 크거나 같다면 삼각형이 아니고
    elif len(s) == 2:
        print('Isosceles')
    # 두 변의 길이가 같으면 이등변 삼각형입니다.
    else:
        print('Scalene')
    # 그 외의 경우는 모든 변이 다른 삼각형입니다.