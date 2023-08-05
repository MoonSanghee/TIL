most = 0
# 최댓값을 저장해줄 변수를 만들어줍니다.
now = 0
# 현재 열차의 인원을 저장할 변수를 만들어줍니다.
for _ in range(10):
    # 10번의 정거장으로 지나며
    left, come = map(int, input().split())
    # 타고 내리는 인원을 받아줍니다.
    now += come
    now -= left
    # 현재 인원에 타는 사람을 더하고 내리는 사람을 빼줍니다.
    most = max(most, now)
    # 현재값과 최댓값을 비교하여 최대값을 갱신하여줍니다.
print(most)
# 최댓값을 출력해줍니다.