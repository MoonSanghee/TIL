n, m = map(int, input().split())
# 주어지는 숫자의 개수와 출력할 조합의 길이를 받아줍니다.
nums = sorted(list(map(int, input().split())))
# 
visited = [False] * n
# n개의 수를 받고 사용하였는지 표시해줄 n개의 boolean 값을 가진 리스트를 만들어줍니다.
li = []
# 조합을 저장할 빈 리스트를 만들어줍니다.

def dfs():
    if len(li) == m:
        print(*li)
        return
    # 리스트의 길이가 원하는 만큼 길어졌다면 리스트 안의 값들을 출력해줍니다.
    used = 0
    # 한 자리에 같은 값은 한 번만 쓰면 되기때문에 사용해준 값인지 확인하기 위한 값을 설정해줍니다.
    for i in range(n):
        if not visited[i] and used != nums[i]:
            # 주어진 수중 같은 자리에서 사용한 적이 없는 수인지와 nums에서 사용한 적있는 수인지 확인해줍니다.
            visited[i] = True
            li.append(nums[i])
            used = nums[i]
            # 방문처리를 해주고 조합 리스트에 수를 넣어준 다음 그 자리에 사용하였음을 표시해주고
            dfs()
            # 재귀를 실행해준다음
            visited[i] = False
            li.pop()
            # 방문을 해제하고 리스트에 값을 빼줍니다.

dfs()
# 정의한 함수를 호출하여줍니다.