import sys
input = sys.stdin.readline

n, q = map(int, input().split())
numbers = list(map(int, input().split()))
# 수열의 길이와 질문의 개수를 받아줍니다.
numbers.sort()
# 수열을 오름차순으로 정렬해줍니다.
new = [0]
# 각 자리까지 합을 담을 리스트를 만들고 0을 담아줍니다.
for i in numbers:
    new.append(new[-1] + i)
    # 각 자리까지 연속 합의 마지막 수에 다음 수를 더하며 합 리스트를 완성시켜줍니다.

for _ in range(q):
    l, r = map(int, input().split())
    print(new[r] - new[l - 1])
    # 수열의 시작과 끝자리를 받고 연속합 리스트에서 찾은 값을로 주어진 범위 합을 구하여 출력해줍니다.