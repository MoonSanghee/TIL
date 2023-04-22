n, k = map(int, input().split())
# 범위와 k번째 지울 수를 입력받습니다.
nums = [0 for _ in range(n + 1)]
# n까지 수중 방문처리를 할 리스트를 만들어줍니다.
cnt = 0
# 몇 번째 지우는 수인지 표시할 cnt를 만들어줍니다.
for i in range(2, len(nums) + 1):
    # 2부터 소수들을 차례로 확인하여줍니다.
    for j in range(i, n + 1, i):
        # n까지 소수 i의 간격으로 모든 수를 확인합니다.
        if not nums[j]:
            # 아직 나온적 없는 수라면
            nums[j] = 1
            cnt += 1
            # 리스트에 나왔다는 표시를 해주고 수를 세어줍니다.
            if cnt == k:
                print(j)
                # cnt가 k에 도달하면 j를 출력하고 연산을 멈추어줍니다.
                break