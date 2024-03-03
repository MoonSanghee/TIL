n, c, w = map(int, input().split())
# 나무의 수와 자르는데 필요한 비용, 단위당 가격을 받아줍니다.
price = 0
trees = [int(input()) for _ in range(n)]
# 최종 가격을 담을 변수를 설정해주고 나무의 길이를 리스트에 담아줍니다.

for i in range(1, max(trees) + 1):
    # 1부터 가장 긴 나무 길이까지 잘라서 얼마를 벌 수 있는지 확인할 것이므로 
    # 가장 긴 나무 +1 까지 범위를 탐색해줍니다.
    total = 0
    # 나무를 특정 크기로 잘랐을 때 기대 수익을 담을 변수를 만들어줍니다.
    for tree in trees:
        if i <= tree:
            # 나무가 자르고자하는 크기보다 작을경우 쓸 수 없으므로 원하는 크기 이상의 나무만 자릅니다.
            get = tree // i
            # 원하는 크기만큼 나무가 얼마나 나오는지 구하고
            income = get * w * i
            # 그 크기만큼 나무를 잘랐을 때 판매 금액을 구해줍니다.
            if tree % i:
                cost = get * c
            else:
                cost = (get - 1) * c
            # 짜투리가 없다면 더미의 개수에 1개 뺀 만큼 자르면되고 짜투리가 있다면 얻게되는 더미만큼 잘라야합니다.
            if income >= cost:
                total += income - cost
                # 기대 수익이 자르는데 필요한 금액 이상이라면 기대 수익에 대해줍니다.
    price = max(price, total)
    # 기대 수익을 최고 금액과 비교하여 갱신해줍니다.

print(price)
# 최고로 얻을수 있는 수익을 출력해줍니다.