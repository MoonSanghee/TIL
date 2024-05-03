num = [True] * 1001
prime = []
# 1000이하의 소수를 확인하기위해 1001개의 True값이 담긴 리스트를 만들어줍니다.
for i in range(2, 34):
    if not num[i]:
        continue
    for j in range(i * 2, 1001, i):
        num[j] = False
# 1000의 32의 제곱보다 크고 33의 제곱보다 작으므로 1000이하의 2의 배수부터 33의 배수까지를 확인하여 소수가 아니라고 표시해줍니다.
for i in range(2, 1001):
    if num[i]:
        prime.append(i)
# 1000이하의 소수를 확인하여 빈 리스트에 담아줍니다.
coms = {}

for i in prime:
    for j in prime:
        for k in prime:
            result = i + j + k
            if result not in coms:
                coms[result] = [i, j, k]
# 1000 이하의 소수 3개를 더해서 나오는 결과값과 합 조합에 사용된 세 수의 리스트를 키, 밸류로 딕셔너리에 담아줍니다.
n = int(input())
# 확인할 수의 개수를 받아줍니다.
for _ in range(n):
    k = int(input())
    if k in coms:
        print(*coms[k])
    else:
        print(0)
    # 수를 받아 만들어질수 있는지 확인하고 결과를 출력해줍니다.