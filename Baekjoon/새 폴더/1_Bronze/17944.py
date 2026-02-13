n, t = map(int, input().split())
cycle = []
# 주어지는 변수들을 받고 사이클을 담을 변수를 만들어줍니다
for i in range(n * 2):
    cycle.append(i + 1)
# 필요한 팔이 2n이 될때까지 리스트에 넣어줍니다
for i in range(1, n * 2 - 1):
    cycle.append(2 * n - i)
# 필요한 팔이 2개가 될때까지 넣어줍니다
t -= 1
t %= (len(cycle))
# 인덱스값과 맞춰주기위해 t에서 1을 빼고 사이클의 길이로 나눈 나머지를 구해줍니다
print(cycle[t])
# 결과를 출력해줍니다