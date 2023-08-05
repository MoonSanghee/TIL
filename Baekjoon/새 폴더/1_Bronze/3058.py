t = int(input())
# 시행회수를 받아줍니다.
for tc in range(t):
    nums = list(map(int, input().split()))
    # 7개의 정수를 받아줍니다.
    even = []
    # 짝수를 담을 리스트를 만들어줍니다.
    for num in nums:
        if not num % 2:
            even.append(num)
            # 짝수를 리스트에 담아줍니다.
    print(sum(even),min(even))
    # 짝수의 합과 가장 작은 짝수를 차례로 출력해줍니다.