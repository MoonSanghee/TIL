n, k = map(int, input().split())
tracks = list(map(int, input().split()))
cnt = 0
# 두 정수 n과 k, 최초 트랙의 상태를 받고 트랙을 몇 번 바꾸는지 담을 변수를 설정해줍니다
for i in range(1, n):
    if tracks[i - 1] < tracks[i]:
        continue
    # 트랙이 길어졌다면 다음으로 넘어갑니다
    else:
        if tracks[i - 1] < tracks[i] + k:
            tracks[i] += k
            cnt += 1
        # 트랙이 길어지지 않았지만 k만큼 늘려 길어질수있다면 k만큼 늘리고 변경회수를 갱신해줍니다
        else:
            print(-1)
            break
        # 늘어날수 없다면 -1을 출력하고 멈추어줍니다
else:
    print(cnt)
# 계속 증가하는 트랙을 만들었다면 트랙을 바꾼 회수를 출력해줍니다