nums, wants = map(int, input().split())
li = list(map(int, input().split()))
s = 0
e = 0
result = 0
length = 100001
while True:
    if e in range(nums):
        if result < wants:
            result += li[e]
            e += 1
        else:
            result -= li[s]
            s += 1
        if result >= wants:
            if length > e - s:
                length = e - s
    else:
        if result >= wants:
            result -= li[s]
            s += 1
        if result >= wants:
            if length > e - s:
                length = e - s
        else:
            break
if length == 100001:
    print(0)
else:
    print(length)
# 문제를 잘못 읽어 원하는 결과보다 크면서 가장 원하는 수에 가까운 경우를 찾는 코드를 찾다가
# 많은 실패를 겪었습니다. 문제를 제대로 천천히 똑바로 읽도록 노력이 필요 할 것 같습니다.
# 범위의 마지막 지점을 기준으로 코드를 작성한 탓인지 확인하는 과정이 불필요하게 많이 사용된것같습니다.
# 범위의 시작 지점을 기준으로 코드를 다시 짜봐야겠습니다.