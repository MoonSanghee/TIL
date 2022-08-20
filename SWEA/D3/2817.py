import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(idx,sum):
    global cnt
    visited[idx] = 1
    sum += numbers[idx]
    if sum == tarket:
        cnt += 1
    for i in range(idx,n):
        if not visited[i]:
            dfs(i,sum)
            visited[i] = 0

test_case = int(input())
for test in range(1, test_case + 1):
    n, tarket = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        visited = [0] * n
        dfs(i, 0)
    print('#{} {}'.format(test, cnt))


# combinations 함수를 불러와서 푸는 코드
# from itertools import combinations

# t = int(input())
# for tc in range(1, t + 1) :
#     n, k = map(int, input().split())
#     data = list(map(int, input().split()))
#     result = 0
#     for i in range(1, len(data) + 1) :
#         for value in combinations(data, i) :
#             if sum(value) == k :
#                 result += 1

#     print('#%d %d' % (tc, result))