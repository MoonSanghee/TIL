n, q = map(int, input().split())
# 손풍기의 수와 시간을 받아줍니다
result = [0, float('inf')]
# 결과를 담을 변수를 설정해줍니다
for i in range(n):
    p, k, c = map(int, input().split())    
    # 구매비용과 충전 주기와 충전비용을 받아줍니다
    cnt = (q - 1) // k
    total = cnt * (cnt + 1) // 2
    price = p + total * c
    # 등차 수열의 합을 이용하여 전체 비용을 구하여줍니다

    if price < result[1]:
        result[0] = i + 1
        result[1] = price
    # 이전 최소비용보다 저렴하다면 비용과 손풍기의 번호를 갱신해줍니다
print(*result)
# 결과를 출력해줍니다