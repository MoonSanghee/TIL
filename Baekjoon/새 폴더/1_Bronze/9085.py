t = int(input())
# 테스트를 몇 번 진행하는지 받아줍니다.
for _ in range(t):
    n = int(input())
    # 받을 수의 개수를 받아줍니다.
    nums = list(map(int, input().split()))
    # 더할 수들을 받아줍니다.
    print(sum(nums))
    # 수의 합을 출력해줍니다.