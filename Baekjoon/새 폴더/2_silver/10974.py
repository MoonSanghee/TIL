n = int(input())
li = []
def dfs():
    if len(li) == n:
        print(*li)
        return
    for i in range(1, n + 1):
        if i not in li:
            li.append(i)
            dfs()
            li.pop()

dfs()

# 재귀를 이용하여 1부터 n+1 까지를 반복하며 리스트에 없으면 값을 추가해주고 함수를 실행 시킨 후 
# 값을 pop하여주어 li의 길이가 n이 될때까지 반복하여 n의 길이가 되면 값을 출력해줍니다.