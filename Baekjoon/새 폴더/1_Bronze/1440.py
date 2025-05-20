from itertools import permutations
# 순열을 불러와줍니다
def check(h, m, s):
    return 1 <= h <= 12 and 0 <= m <= 59 and 0 <= s <= 59
# 시계가 유효한지 확인하기 위한 함수를 만들어줍니다
time = list(map(int, input().split(":")))
count = 0
# 주어지는 시계를 받고 유효한 시간의 개수를 담을 변수를 설정해줍니다
for perm in permutations(time):
    h, m, s = perm
    if check(h, m, s):
        count += 1
    # 순열의 모든 조합을 확인하여 유효한 시간의 수를 확인해줍니다
print(count)
# 결과값을 출력해줍니다
