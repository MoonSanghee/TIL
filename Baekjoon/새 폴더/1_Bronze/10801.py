A = list(map(int, input().split()))
B = list(map(int, input().split()))
# 두 사람이 가진 카드를 받습니다.
result = 0
for i in range(10):
    if A[i] > B[i]:
        result += 1
    elif A[i] < B[i]:
        result -= 1
# 승부 결과에따라 A가 이기면 result에 1점 더해주고 B가 이기면 1점을 빼줍니다.
if result > 0:
    print('A')
elif result < 0:
    print('B')
else:
    print('D')
# 결과에 따라 값을 출력해줍니다.