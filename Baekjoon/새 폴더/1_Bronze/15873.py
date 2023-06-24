nums = str(input())
# 연속된 숫자를 문자열로 받아줍니다.
if len(nums) == 2:
    # 길이가 2라면 두 숫자는 한자리 숫자이니 두 수를 나누어줍니다.
    a, b = nums[0], nums[1]
elif len(nums) == 3:
    # 길이가 3이라면
    if nums[1] == '0':
        a,b = nums[:2], nums[2]
        # 가운데 문자가 '0'이라면 10과 한자리 숫자로 이루어져있고
    else:
        a, b = nums[:1], nums[1:]
        # 아니라면 한 자리 숫자와 10으로 이루어져있고
else:
    a, b = 10, 10
    # 길이가 4라면 10 두개로 이루어졌있습니다.
print(int(a) + int(b))
# a, b를 합친 값을 출력해줍니다.