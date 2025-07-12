n = int(input())
# 참가하는 학생의 수를 받아줍니다
result = 601
# 각운동의 최대 기록은 200이므로 합은 600이하이기때문에 결과에 600보다 큰 수를 담아줍니다
for _ in range(n):
    total = sum(list(map(int, input().split())))
    if total >= 512:
        result = min(result, total)
    # 학생들의 기록을 받아 결과가 512이상이라면 result값을 갱신해줍니다

if result == 601:
    print(-1)
else:
    print(result)
    # result값이 한 번도 갱신된 적이 없다면 -1을 갱신된적이 있다면 담긴값을 출력해줍니다