n, m = map(int, input().split())
numbers = list(map(int, input().split()))
# 두 수와 수열을 받아줍니다.
numbers.sort()
coms = []
# 수열을 오름차순으로 정렬하고 조합을 만들 빈 리스트를 만들어줍니다.
def dfs():
    if len(coms) == m:
        print(*coms)
        return
    # 조합이 원하는 길이를 만족하였다면 출력하여줍니다.
    used = 0
    # 사용한 수인지 확인할 변수를 정해줍니다.
    for i in range(n):
        if used != numbers[i]:
            # 사용한 적 없는 수라면
            coms.append(numbers[i])
            used = numbers[i]
            # 조합에 수를 추가하고 사용하였음을 표시해줍니다.
            dfs()
            coms.pop()
            # 재귀를 실행해주고 조합에 들어간 수를 빼줍니다.

dfs()