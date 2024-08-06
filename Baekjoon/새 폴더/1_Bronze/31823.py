n, m = map(int, input().split())
# 동아리원의 수와 확인할 일수를 받아줍니다.
results = []
count = set()
# 동아리원들의 기록을 담을 리스트와 연속으로 문제를 풀지않은 날을 담을 세트형을 만들어줍니다
for _ in range(n):
    record = list(input().split())
    # 기록을 받아줍니다.
    best = 0
    cnt = 0
    # 개인의 최고 연속해서 문제를 풀지않은 날과 현재 연속한 문제 풀지 않은날을 담을 변수를 설정해줍니다.
    for i in record:
        if i == '.':
            cnt += 1
            best = max(best, cnt)
        else:
            cnt = 0
        # 문제를 풀지 않았다면 cnt를 갱신해주고 best를 비교하여 갱신해주고
        # 문제를 풀었다면 cnt값을 0으로 설정해줍니다.
    
    count.add(best)
    results.append((best, record[m]))
    # count에 best에 result에 기록을 담아줍니다.

print(len(count))
for result in results:
    print(*result)
# 결과를 출력해줍니다.