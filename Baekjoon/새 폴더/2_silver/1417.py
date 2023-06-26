import heapq
# 힙 자료구조를 이용하여 나머지 후보중 가장 높은 값을 빼서 비교해줄것입니다.
n = int(input())
# 후보의 수를 받아줍니다.
win = int(input())
# 이기기 위해 가장 높은 수를 가져야하는 득표를 받아줍니다.
nums = []
# 나머지 후보의 득표를 받아줄 리스트를 만듭니다.
for _ in range(n - 1):
    num = int(input())
    heapq.heappush(nums, (-num, num))
    # 나머지 후보의 득표를 nums에 heapqpush해줍니다.

cnt = 0
# 표를 몇 번 옮겼는지 기록해줄 변수를 선언해줍니다.
while nums:
    # 다솜이보다 득표가 많은 후보가 리스트에 남았다면 계속해줘야합니다.
    num = heapq.heappop(nums)[1]
    if num >= win:
    # heappop을 통해 뺀 값이 다솜이의 현재 득표보다 많거나 같다면
        num -= 1
        win += 1
        cnt += 1
        # 1표를 다솜이에게 옮기고 
        heapq.heappush(nums, (-num, num))
        # 바뀐 득표를 힙에 넣어줍니다.

print(cnt)
# 옮긴 횟수를 출력해줍니다.