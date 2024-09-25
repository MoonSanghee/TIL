n, s, r = map(int, input().split())
# 참가팀의 수와 부서진 카약의 수 예비 카약의 수를 받아줍니다. 
broken = list(map(int, input().split()))
reserve = list(map(int, input().split()))
broken, reserve = list(set(broken) - set(reserve)), list(set(reserve) - set(broken))
# 카약이 부서진 팀과 예비를 챙겨온 팀을 받고 부서진 팀중 예비 카약이 있는 팀을 제거해줍니다.
result = 0

for i in broken:
    if i - 1 in reserve:
        reserve.remove(i - 1)
    elif i + 1 in reserve:
        reserve.remove(i + 1)
    else:
        result += 1
    # 카약을 빌릴수 있는지 확인하고 못 빌린다면 참가 못하는팀의 값을 갱신해줍니다.

print(result)
# 참가 못하는 팀의 수를 출력해줍니다.