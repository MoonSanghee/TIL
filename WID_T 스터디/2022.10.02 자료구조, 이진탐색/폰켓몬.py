def solution(nums):
    answer = 0
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
    if len(d) > len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(d)
        
    return answer