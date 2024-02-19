n, m = map(int, input().split())
budget = [int(input()) for _ in range(n)]
# 용돈을 사용할 날과 인출 횟수 용돈을 사용할 금액을 차례대로 받아줍니다.
l, r = min(budget), sum(budget)
# 최소 금액은 가장 적은 용돈을 사용하는 날로 최대 금액은 전체 용돈의 합으로 설정해줍니다.

while l <= r:
    # 범위를 확인 할 수 없을때까지 계속합니다. 
    mid = (l + r) // 2
    pocket = mid
    cnt = 1
    # 최소 금액과 최대 금액의 절반 지점을 확인하기위해 둘을 합하여 2로 나눈 중위값을 구하고
    # 그 금액 만큼 출력하여 변수에 담은 후 1번 출금하였음을 표시해줍니다.
    for i in budget:
        # 용돈을 순회하며
        if pocket < i:
            pocket = mid
            cnt += 1
            # 남은 용돈이 필요한 금액보다 적다면 용돈을 새로 출금하니 값을 갱신하고 출금 횟수를 수정해줍니다.
        pocket -= i
        # 사용한 용돈을 차감해줍니다.

    if cnt > m or mid < max(budget):
        l = mid + 1
        # 출금 횟수가 제한보다 많거나 중위 금액이 최대 사용하는 용돈보다 작다면 확인 범위의 시작점을 갱신하고
    else:
        r = mid - 1
        k = mid
        # 아니라면 최대금액을 갱신하고 찾는 금액값을 수정해줍니다.

print(k)
# 연산이 끝나고 k에 담긴 값을 출력해줍니다.