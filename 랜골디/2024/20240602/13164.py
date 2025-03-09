n, k = map(int, input().split())
kids = list(map(int, input().split()))
# 원생의 수와 나눌 그룹의 수를 받고 원생의 키를 받아줍니다.
costs = []
for i in range(n - 1):
    costs.append(kids[i + 1] - kids[i])
# 연속한 원생이 같은 조에 들어갈때 티셔츠를 만드는데 필요한 비용을 리스트에 담아줍니다.
costs.sort(reverse = True)
# 비용을 내림차순으로 정렬해줍니다.
print(sum(costs[k - 1:]))
# k개의 조로 나누기 위해서는 k - 1개의 연결되지 않은 부분이 필요하므로 비용의 k - 1번째부터의 합을 출력해줍니다.