N, L, D = map(int, input().split())
total = N * L + (N - 1) * 5 
# 앨범의 총 길이 구해줍니다.
song = [False] * total 
# 노래가 나오는 시간대을 확인해줍니다.
for i in range(0, total, L + 5): 
    # 각 노래는 0 초부터 시작하는 간격을 주기로
    for j in range(i, i + L): 
        song[j] = True
        # 노래가 나오는 시간을 확인해줍니다.
for i in range(0, total, D): 
    if not song[i]:
        print(i)
        break
    # 전화가 올 때 노래가 울리는지 확인해줍니다.
else:
    print(i + D)