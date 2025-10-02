t = int(input())
# 테스트 케이스의 수를 받아줍니다
for _ in range(t):
    n = int(input())
    # 카드의 개수를 받아줍니다
    memory = list(input().split())
    cards = list(input().split())
    memory.sort()
    cards.sort()
    # 기억한 카드와 제출한 카드를 받고 사전순으로 정렬해줍니다
    if memory != cards:
        print("CHEATER")
    else:
        print("NOT CHEATER")
    # 둘을 비교하여 바꿔치기를 하였는지 출력해줍니다