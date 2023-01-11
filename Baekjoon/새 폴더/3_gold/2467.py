n = int(input())
nums = list(map(int, input().split()))
# 입력받을 수의 개수와 숫자들을 저장해줍니다.
s = 0
e = n - 1
# 시작점과 끝점을 저장해줍니다.
com = [nums[0], nums[e]]
# 시작점과 끝점을 리스트로 묶어줍니다.
minimum = 10**10
# 두 수를 합쳐 절대값으로 나올수 있는 최대값보다 큰 수를 저장해줍니다.
while s < e:
    # 두 수가 만날때까지 돌려줍니다.
    if abs(nums[s] + nums[e]) <= minimum:
        com = [nums[s], nums[e]]
        minimum = abs(sum(com))
        # 두 지점의 합이 지금 저장된 가장 작은 합보다 작으면 합과 조합을 갱신해줍니다.
    if abs(nums[s]) > abs(nums[e]):
        s += 1
    else:
        e -= 1
        # 시작점과 끝점의 절대값을 비교하여 더 큰 값을 1칸 움직여줍니다.
print(*com)
# 조합의 인덱스값들을 출력해줍니다.