N, W, H, L = map(int, input().split())
# 4 변수를 받아줍니다.
print(min((W//L)*(H//L), N))
# 총 소의 수와 최대로 들어갈 수 있는 소의 수를 비교하여 작은쪽을 출력해줍니다.