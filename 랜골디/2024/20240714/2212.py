n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
# 센서와 집중국의 개수를 받고 센서의 위치를 받아줍니다.

if k >= n:
    print(0)
    # k가 n이상이라면 모든 센서위에 집중국을 설치할수 있으므로 0을 출력해줍니다.
else:
    sensors.sort()
    distances = []
    # 센서를 정렬하고 센서 사이의 거리를 담을 리스트를 만들어줍니다.
    for i in range(n - 1):
        distances.append(sensors[i + 1] - sensors[i])
    # 센서사이의 거리를 리스트에 담아줍니다.
    distances.sort()
    # 센서 사이의 거리를 리스트에 담고 사이 거리가 담긴 리스트를 정렬해줍니다.
    for _ in range(k - 1):
        distances.pop()
        # k 개의 집중국을 설치해서 k - 1개의 간격이 사라지므로 
        # arr에서 가장큰 k - 1개의 값을 빼줍니다.

    print(sum(distances))
    # arr의 합을 출력해줍니다.