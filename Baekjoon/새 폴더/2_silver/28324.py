n = int(input())
numbers = list(map(int, input().split()))
# 지나갈 구역의 길이와 각 구역의 속력 제한을 받아줍니다
numbers = numbers[::-1]
numbers[0] = 1
# 마지막 구역만 제한 속력이 있으므로 주어진 제한 속력 리스트를 뒤집고 첫 값을 1로 수정해줍니다
for i in range(1, n):
    numbers[i] = min(numbers[i], numbers[i - 1] + 1)
# 각 구역의 제한속력를 이전 구역에서 1 증가 시킨것과 기존값을 비교해 작은 값으로 갱신해줍니다
print(sum(numbers))
# 속력의 합을 출력해줍니다