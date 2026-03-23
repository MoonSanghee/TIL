N = int(input())
result = 0
# 주어지는 수를 받고 결과를 담을 변수를 설정해줍니다
for i in range(N):
    if N - i < i:
        break
    # N - i 가 i보다 작아진다면 손을 바꾸어 같은 조합을 이루므로 반복을 멈추어줍니다
    elif i <= 5 and N - i <= 5:
        result += 1
    # 양손 모두 5개 이하일 경우만 결과에 더해줍니다
print(result)
# 결과를 출력해줍니다