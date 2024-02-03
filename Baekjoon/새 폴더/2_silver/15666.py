n, m = map(int, input().split())
# n, m을 받아줍니다.
numbers = sorted(list(set(list(map(int, input().split())))))
# n개의 수를 받아줍니다.
com = []
# 조합을 담을 변수를 정해줍니다.
def dfs(a):
    if len(com) == m:
        return print(*com)
    # com에 원하는 길이의 조합이 완성되었다면 출력해줍니다.
    for i in range(a, len(numbers)):
        com.append(numbers[i])
        dfs(i)
        com.pop()
    # com에 numbers[i]부터 이후에오는 수를 담고 재귀를 실행한 뒤 pop을 해줍니다.

dfs(0)
# 함수를 실행시켜 줍니다