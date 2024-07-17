n = int(input())
# 카드의 수를 받아줍니다.
J = list(map(int, input().split()))
owner = list(map(int, input().split()))
# 주언이와 사장님의 카드를 받아줍니다.
J.sort()
owner.sort()
# 주언이와 사장님이 가진 카드를 오름차순으로 정렬해줍니다.
result = 0
idx = 0
# 게임의 결과를 담을 변수와 주언이가 사용할수있는 가장 작은값 카드를 담을 변수를 설정해줍니다.
for i in range(n):
    if J[idx] < owner[i]:
        result += 1
        idx += 1
        # 주언이가 낼 카드가 사장님이 낼 카드보다 값이 작으면 result에 1을 더하고 카드를 사용했으니 인덱스를 1 이동시켜줍니다.
    else:
        result -= 1
        # 주언이가 낼 카드가 사장님이 낼 카드보다 크면 result에 1을 빼줍니다.

if result > 0:
    print('YES')
else:
    print('NO')
    # 예측 결과를 출력해줍니다.