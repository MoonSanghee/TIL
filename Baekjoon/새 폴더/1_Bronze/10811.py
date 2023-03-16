n, m = map(int, input().split())
# 바구니의 개수와 몇 번 뒤집을것이니 받아줍니다.
baskets = [i for i in range(1, n + 1)]
# 바구니 n개를 1부터 차례대로 이름붙여줍니다.

for _ in range(m):
    s, e = map(int, input().split())
    # 뒤집기을 바구니의 범위, 시작과 끝 점을 받아줍니다.
    front = baskets[:s - 1]
    # basktes의 시작은 s이미로 s 직전의 바구니까지를 앞에 위치하는 front로 이름지어줍니다.
    re = baskets[s - 1:e][::-1]
    # s번 바구니부터 뒤집을것이기에 s - 1번 인덱스부터 e - 1번 인덱스까지의 바구니를
    # 뒤집은것을 re라고 이름지어줍니다. 
    end = baskets[e:]
    # 뒤집은 바구니 이후에 오는 바구니들을 마지막에오는 end로 이름붙여줍니다.
    baskets = front + re + end
    # 바구니의 나열을 변하지 않은 front와 end 사이에 뒤집은 re를 합친 형태로 이름지어줍니다.
print(*baskets)
# 새로 정렬한 바구니의 형태를 출력하여줍니다.