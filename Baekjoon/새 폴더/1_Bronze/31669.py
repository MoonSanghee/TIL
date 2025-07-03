n, m = map(int, input().split())
arr = [[] for _ in range(m)]
# 주어지는 수업의수와 선생님의 수를 받고 수업시간별로 선생님이 도는지 확인할 이중리스트를 만들어줍니다
for _ in range(n):
    line = input()
    for i in range(m):
        arr[i].append(line[i])
    # 각 선생님의 순찰 일정을 받아 수업 시간별로 넣어줍니다
for i in range(m):
    if "O" not in arr[i]:
        print(i + 1)
        break
    # 선생님이 순찰을 돌지않는 시간이 있다면 가장 빠른것을 출력하고 반복을 멈추어줍니다
else:
    print("ESCAPE FAILED")
    # 없다면 탈출 실패를 출력해줍니다