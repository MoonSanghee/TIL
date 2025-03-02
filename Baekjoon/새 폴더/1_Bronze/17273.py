n, m = map(int, input().split())
front = []
back = []
now = [0] * n
result = 0
# n, m을 받고 카드의 앞면과 뒷면을 담을 리스트와 현재 앞면인지 뒷면인지를 나타낼 리스트를 만들고 최종 합을 담을 변수를 설정해줍니다
for _ in range(n):
    f, b = map(int, input().split())
    front.append(f)
    back.append(b)
# 카드의 앞뒤면을 차례대로 받아 넣어줍니다
for _ in range(m):
    called = int(input())
    for i in range(n):
        if now[i] == 0:
            check = front[i]
        else:
            check = back[i]
        if check <= called:
            now[i] += 1
            now[i] %= 2
# m번의 수를 받아 카드의 값이 받은 수 이하라면 뒤집어줍니다
for i in range(n):
    if now[i]:
        result += back[i]
    else:
        result += front[i]
print(result)
# 모든 카드 값을 합하여 결과를 출력해줍니다