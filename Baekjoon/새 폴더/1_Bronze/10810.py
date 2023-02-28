n, m = map(int, input().split())
# 바구니와 공을 몇 번 넣을것인지 받아줍니다.

basket = [0 for _ in range(n)]
# 공의 개수만큼 비었다는 표시로 0을 인덱스 값으로한 리스트를 만들어줍니다.

for _ in range(m):
    s, e, num = map(int, input().split())
    for i in range(s - 1, e):
        basket[i] = num
        # 공을 넣는 횟수만큼 바구니의 시작과 마지막까지 공의 번호로 바꾸어주고

print(*basket)
# 바구니에 들어가있는 상태를 출력해줍니다.