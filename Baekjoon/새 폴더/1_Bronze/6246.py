n, q = map(int, input().split())
slots = [1 for _ in range(n + 1)]
slots[0] = 0
# 슬롯의 수와 풍선을 놓을 횟수를 받고 n + 1길이의 슬롯을 만들고 0번 슬롯을 비워줍니다
for _ in range(q):
    l, i = map(int, input().split())
    for j in range(l, n + 1, i):
        slots[j] = 0
# 주어지는 조건대로 풍선이 놓일 슬롯을 비워줍니다
print(sum(slots))
# 풍선이 없는 슬롯의 합을 출력해줍니다