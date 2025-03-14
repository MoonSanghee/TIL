n = int(input())
stones = 0
add = 1
# 최초 주어지는 돌의 개수를 받고 각 차례에 추가될 돌의 개수 차례가 끝날때 돌의 개수를 담을 변수를 설정해줍니다
while stones <= n:
    stones += add
    add += 1
# 돌의 개수가 충분해질때까지 게임을 진행해줍니다
if add % 2:print(0)
else:print(stones - n)
# 추가해야할 돌의 개수가 홀수라면 푸앙이의 차례이므로 친구가 이길수 없고 짝수라면 필요한 돌의 개수를 출력해줍니다