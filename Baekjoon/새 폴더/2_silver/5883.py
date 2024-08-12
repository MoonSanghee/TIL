n = int(input())
# 줄의 길이를 받아줍니다.
line = [int(input()) for _ in range(n)]
# 줄의 상태를 받고
kinds = set(line)
# 용량의 종류를 받아줍니다.
result = 1
# 결과를 담을 변수를 설정합니다
for kind in kinds:
    # 각 용량을 차례대로 빼서 확인해줍니다
    cnt = 1
    i = 0
    # 현재 연속한 줄의 길이와 이전에 확인한 위치를 담을 변수를 설정해줍니다.
    for j in range(1, n):
        if line[j] == kind:
            continue
        # line[j]와 kind 값이 같다면 kind를 뺀 상태를 확인하는중이므로 continue를 이용해 다음으로 넘어갑니다
        if line[i] == line[j]:
            cnt += 1
            result = max(result, cnt)
        else:
            cnt = 1
        # 줄이 연속하다면 값을 증가시키고 reuslt값을 갱신해주고 연속하지 않다면 cnt값을 1로 갱신해줍니다.
        i = j
        # 이전 확인한 줄의 위치를 갱신해줍니다.

print(result)
# 결과를 출력해줍니다.