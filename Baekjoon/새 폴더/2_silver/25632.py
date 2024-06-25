a, b = map(int, input().split())
c, d = map(int, input().split())
# 두 사람이 가지는 범위를 받아줍니다.
prime = []
# 1000이하의 소수를 리스트에 담아줍니다.
for i in range(2, 1001):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        prime.append(i)

yt = 0
yj = 0
both = 0
# 용태와 유진이가 가지는 수의 개수와 두 사람 다 가지는 수의 개수를 담을 변수를 설정해줍니다. 
for i in prime:
    if a <= i <= b and c <= i <= d:
        both += 1
    elif a <= i <= b:
        yt += 1
    elif c <= i <= d:
        yj += 1
# 소수를 순회하면 범위안의 소수를 가지는지 확인해줍니다.
if both % 2:
    yt += 1
# 공통으로 가지는 소수가 홀수라면 용태가 공통된 소수중 마지막 수를 사용할 수 있으니 용태의 수를 1개 더 가지고있다고 해줍니다. 
if yt > yj:
    print('yt')
else:
    print('yj')
# 게임의 결과를 출력해줍니다.