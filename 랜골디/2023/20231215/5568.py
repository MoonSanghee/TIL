n = int(input())
k = int(input())
# 카드의 개수와 뽑을 카드의 개수를 받아줍니다.
numbers = []
visited = [False] * n
for _ in range(n):
    numbers.append(input())
# 카드를 받아주고 카드를 뽑았는지 확인할 카드 개수의 길이의 False를 값으로 가지는 리스트를 만들어줍니다.

coms = []
# 조합을 담을 리스트를 만들어줍니다.

def dfs(num, cnt):
    if cnt == k:
        coms.append(num)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(num + numbers[i], cnt + 1)
            visited[i] = False
# 원하는 카드의 개수만큼 카드를 뽑은적 없는지 확인하여 뽑고 충분히 뽑았다면 조합을 리스트에 담는 함수를 만들어줍니다.

dfs('', 0)
# 함수를 실행시켜 카드를 뽑아 만들수 있는 조합을 구해줍니다.

coms = list(set(coms))
# 중복을 제거합니다.

print(len(coms))
# 조합의 길이를 출력합니다.