n = int(input())
nums = list(map(int, input().split()))
# 수의 개수와 각 수의 앞에 위치하는 더 큰 수들의 개수를 받아줍니다.

new = [0 for _ in range(n)]
# 새로 수를 나열할 리스트를 만들어줍니다.
# 이 때 리스트의 크기는 n이고 각 인덱스 값은 0으로 만들어줍니다.

for i in range(1, n + 1):
    num = nums[i - 1]
    cnt = 0
    # nums의 i - 1번째 값을 확인하고 더 큰 수가 몇개 나왔는지 세어줄 변수를 지정해줍니다.
    for j in range(n):
        # new 리스트를 순회하며
        if cnt == num and new[j] == 0:
        # new의 인덱스값이 0이고 현재 수보다 큰 수가 원하는만큼 나왔다면
            new[j] = i
            break
        # 그 자리에 현재 수를 저장하고 다음 수로 넘어갑니다.
        elif new[j] == 0:
            cnt += 1
        # new[j]의 값은 0이지만 앞에 현재 수보다 큰 값이 충분히 안 나왔다면
        # cnt 값을 1만큼 더해줍니다.
print(*new)
# new 리스트에 저장된 값들을 출력해줍니다.