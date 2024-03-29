import sys
input = sys.stdin.readline

s, c = map(int, input().split())
numbers = [int(input()) for _ in range(s)]
# 파와 주문받은 파닭의 수를 받고 파의 길이를 받아 리스트에 담아줍니다.
start = 1
end = 1000000000
# 파의 길이는 1이상 10억 이하이므로 시작과 끝을 각 1과 10억으로 설정해줍니다.
length = 0
# 최대 길이를 담을 변수를 설정해줍니다.
while start <= end:
    mid = (start + end) // 2
    cnt = sum((n // mid) for n in numbers)

    if cnt >= c:
        length = max(length, mid)
        start = mid + 1
    else:
        end = mid - 1
    # 이분탐색을 통해 주문받은 자른 결과 나올 파의 개수가 주문받은 파닭의 수보다 적다면 파의 길이를 더 짧게 자르고 아니면 더 길게 자르며 최대길이를 구해줍니다.

print(sum(numbers) - (c * length))
# 전체 길이에서 파의 개수 * 파닭의 수를 빼 남는 파의 총 길이를 구해줍니다.