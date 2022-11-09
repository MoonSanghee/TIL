n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
li.sort()
result = 0
for i in range(n):
    result += abs(li[i] - i - 1)
print(result)
# 전체 예상 순위를 오름차순으로 정렬해준 다음 각 자리와 예상 등수와의 차의 절대값을 누적해주어
# 전체 예상 차이 값을 구하였음. 백준 기준 시간초과 나왔으나 sys.stdin.readline을 이용하니 해결됨.