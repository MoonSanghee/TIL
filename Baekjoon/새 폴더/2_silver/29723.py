n, m, k = map(int, input().split())
d = dict()
total = 0
# 주어지는 성적의 수와 필요한 과목, 공개된 과목의 수를 받고 
# 과목별 점수를 넣을 딕셔너리와 공개된 과목의 점수합을 담을 변수를 설정해줍니다
for _ in range(n):
    name, score = input().split()
    d[name] = int(score)
# 과목별 점수를 받아 딕셔너리에 담아줍니다
for _ in range(k):
    name = input()
    total += d[name]
    del d[name]
# 공개된 과목의 점수를 사용하고 딕셔너리에서 제거해줍니다
lefts = sorted(d.items(), key=lambda x : x[1])
low, high = total, total
for i in range(m - k):
    low += lefts[i][1]
    high += lefts[-i - 1][1]
# 남은 과목의 점수를 오름차순으로 정렬하여 가장 작은값과 큰 값부터 더 필요한 과목의 수에 맞게 더하여줍니다
print(low, high)
# 최소점과 최고점을 출력해줍니다