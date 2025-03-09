n, m = map(int, input().split())
cows = list(map(int, input().split()))
result = []
# 주어진 소의 수와 선별할 소의 수 결과를 소수인 합을 담을 리스트를 만들어줍니다.
prime = []
for i in range(2, 10000):
    isPrime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            isPrime = False
            break
    else:
        prime.append(i)
# 최대 1000키로인 소가 9마리까지 있으므로 10000이하의 소수를 모두 확인하여줍니다.
def pick(idx, cnt, h):
    if cnt == m:
        if h in prime:
            result.append(h)
        return
    # 소를 충분히 골랐다면 몸무게 합이 소수인지 확인하여줍니다.
    elif idx == n:
        return
    # 확인하는 인덱스 범위가 벗어나지 않도록 해줍니다.
    else:
        pick(idx + 1, cnt, h)
        pick(idx + 1, cnt + 1, h + cows[idx])
    # 모든 소를 선택하거나 선택하지 않을 수 있습니다.

pick(0, 0, 0)
# 0,0,0으로 소를 선별하는 함수를 실행해줍니다.
result = list(set(result))
result.sort()
# 소를 선별하여 소수가 되는 값을 구하고 set 메서드를 이용해 중복값을 걸러준 다음
# 다시 리스트에 담고 오름차순으로 정렬을 해줍니다.
if result:
    print(*result)
    # 소수가 되는 조합값이 있다면 결과값을 출력해주고
else:
    print(-1)
    # 아니라면 -1을 출력해줍니다