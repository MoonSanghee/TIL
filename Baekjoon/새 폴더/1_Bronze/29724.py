n = int(input())
# 상자의 개수를 받아줍니다
total = 0
weight = 0
# 무게와 가치를 담을 변수를 설정해줍니다
for _ in range(n):
    T, W, H, L = list(input().split())
    # 주어지는 변수들을 받아줍니다
    if T == "B":
        weight += 6000
    # 상자에 배즙이 담겼다면 120g짜리 50개의 무게를 더해줍니다
    else:
        cnt = (int(W) // 12) * (int(H) // 12) * (int(L) // 12)
        # 사과가 들어갈 수 있는 개수를 구하여줍니다
        total += cnt * 4000
        weight += 1000 + 500 * cnt
        # 가격과 무게를 더해줍니다
print(weight)
print(total)
# 전체 무게와 가격을 출력해줍니다