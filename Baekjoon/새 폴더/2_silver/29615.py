n, m = map(int, input().split())
# 줄의 길이와 친구의 수를 받아줍니다.
line = list(map(int, input().split()))
friends = list(map(int, input().split()))
# 줄의 상태와 친구를 받아줍니다.
result = m
# 친구가 모두 대기줄 밖이라면 최대 이동이 필요하므로 m을 이동 횟수로 설정해줍니다.
for i in friends:
    if i in line[:m]:
        result -= 1
# 친구들중에 충분히 있는 친구를 확인해 이동 횟수를 수정해줍니다.
print(result)
# 필요한 이동횟수를 출력해줍니다.