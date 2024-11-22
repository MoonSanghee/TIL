n, k = map(int, input().split())
d = dict()
visited = [False for _ in range(n)]
# 게임에 참여하는 사람의 수와 보성이의 번호를 받고 지목하는 번호를 담을 딕셔너리 변수와 
# 지목한적 있는지 확인할 리스트를 만들어줍니다
for i in range(n):
    d[i] = int(input())
# 각 학생별로 지목하는 학생을 딕셔너리에 담아줍니다
s = 0
cnt = 0
# 진행 횟수와 지목할 사람을 담을 변수를 설정해줍니다
while True:
    if s == k:
        print(cnt)
        break
    # k가 지목할 차례라면 보성이가 지목당한것이므로 진행하는데 몇번의 턴이 걸렸는지 출력해줍니다
    elif visited[s] == True:
        print(-1)
        break
    # 이미 지목했던 학생이 다시 지목하게 되었다면 보성이에게 도달하지않고 순환하고있으므로 보성이에게 도달할수 없습니다
    cnt += 1
    visited[s] = True
    s = d[s]
    # 진행을 1늘려주고 지목했다는것을 표시한뒤 지목할 사람을 고쳐줍니다