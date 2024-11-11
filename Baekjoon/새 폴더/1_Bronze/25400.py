n = int(input())
numbers = list(map(int, input().split()))
# 수열의 길이와 수열을 받아줍니다
target = 1
cnt = 0
# 제자리 상태로 만들기위해 남겨야하는 카드를 담을 변수와 뺀 카드의 수를 담을 변수를 설정해줍니다.
for i in numbers:
    if i != target:
        cnt += 1
    else:
        target += 1
    # 카드열을 순회하며 필요한 카드라면 필요한 값을 다음 값으로 변경해주고 아니라면 빼줍니다

print(cnt)
# 빼야하는 카드의 수를 출력해줍니다