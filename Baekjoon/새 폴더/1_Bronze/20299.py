import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
# 주어지는 세 값을 받아줍니다
arr = []
# 결과를 담을 리스트를 만들어줍니다
for _ in range(n):
    members = list(map(int, input().split()))
    # 팀원들의 레이팅을 받아줍니다
    if sum(members) < k:
        continue
    # 레이팅의 합이 조건보다 낮으면 다음 팀을 확인해줍니다
    else:
        for member in members:
            if member < l:
                break
            # 멤버중에 조건보다 낮은 레이팅이 있다면 다음 팀으로 넘어가줍니다
        else:
            arr += members
            # 모든 멤버들의 레이팅이 충분하다면 팀원들을 결과에 더해줍니다

print(len(arr) // 3)
print(*arr)
# 주어진 조건대로 출력해줍니다