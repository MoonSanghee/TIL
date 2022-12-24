n = int(input())
nums = list(map(int, input().split()))
# 몇 개의 숫자를 입력받고 입력받은 숫자들이 무엇인지 리스트 형태로 받아줍니다.
dp = []
dp.append(1)
# 넣을 수 있는 상자가 최대 몇개인지 저장할 빈 리스트를 만들어주고 처음 위치한 박스는
# 본인만 위치할 수 있으니 1을 넣어줍니다.
for i in range(1, n):
    d = []
    for j in range(i):
        if nums[i] > nums[j]:
            d.append(dp[j] + 1)
    # nums를 순환하며 본인보다 작은 상자는 그 상자에 넣을수 있으니 dp의 인덱스(최대 몇 개의 상자가 들어갈 수 있는지)
    # 에 1을 더한 값을 d라는 리스트에 넣어줍니다.
    if not d:
        dp.append(1)
    else:
        dp.append(max(d))
    # 그 자리보다 앞에 그 자리 값보다 작은 값이 있었다면 d라는 리스트에 저장된 값이 있을것이니
    # 그 중 가장 큰 값을 dp 리스트에 추가해주고 없다면 본인이 가장 작은 박스이니 1을 넣어줍니다.

print(max(dp))
# dp 리스트에서 가장 큰 값을 출력해줍니다.