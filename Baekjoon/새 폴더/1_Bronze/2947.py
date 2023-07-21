nums = list(map(int, input().split()))
# 나무조각들을 받아줍니다.

while True:
    if nums == [1, 2, 3, 4, 5]:
        break
    # 나무 조각들이 1, 2, 3, 4, 5로 정렬되면 멈추어줍니다.
    for i in range(4):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            print(' '.join(map(str, nums)))
        # 앞에 위치한 수가 더 크다면 바로 다음 나무조각과 바꾸고 출력해줍니다.