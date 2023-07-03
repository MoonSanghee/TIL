Kangaroos = list(map(int, input().split()))
# 캥거루 3마리의 위치를 입력받아줍니다.
print(max(Kangaroos[2] - Kangaroos[1] - 1, Kangaroos[1] - Kangaroos[0] - 1))
# 첫 번째와 두번째 캥거루 사이의 거리와 
# 두번째와 마지막 캥거루 사이의 거리중 큰 경우를 출력해줍니다.