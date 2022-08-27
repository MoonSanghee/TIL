import heapq

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(gragh, start):
    distances = {node: float('inf') for node in gragh} # start로 부터의 거리 값을 저장하기 위함
                        #최대 수
    distances[start] = 0 # 시작하는 자리에서 시작하는 자리까지의 거리는 0
    q = []
    heapq.heappush(q, [distances[start], start]) #시작 노드부터 탐색 시작.

    while q: # q가 빌 때까지 탐색
        current_distance, current_destination = heapq.heappop(q)
        # 탐색할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in gragh[current_destination].items():
            distance = current_distance + new_distance          # 해당 노드를 거쳐 갈 때의 거리
            if distance < distances[new_destination]:           # 알고 있는 거리보다 작으면 갱신 
                distances[new_destination] = distance
                heapq.heappush(q, [distance, new_destination])  # 다음 인접 거리를 계산 하기위해 큐에 삽입

    return distances

print(dijkstra(graph, 'A'))
