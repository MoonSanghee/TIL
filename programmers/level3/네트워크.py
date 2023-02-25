
def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    # 방문 처리를 저장할 visited를 만들어줍니다.
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            chain(i, computers, visited)
            answer += 1
            # 모든 컴퓨터를 순회하며 연결된적 없다면 연결 회로들을 확인하고 answer의
            # 값을 1 더해줍니다.
    return answer
    # answer에 누적된 값을 출력해줍니다.

def chain(a, computers, visited):
    for i in range(len(computers[a])):
        # 입력받은 컴퓨터와 연결된 컴퓨터들을 확인합니다.
        if visited[i] == 0:
            if computers[a][i]:
                # 방문한 적 없는데 연결된 컴퓨터가 있다면
                visited[i] = 1
                chain(i, computers, visited)
                # 연결해주고 새로 연결된 컴퓨터와 연결되어있는 컴퓨터를 확인해 줍니다.