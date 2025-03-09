w = int(input())
# 단어의 수를 받아줍니다
keep_going = set()
wants = dict()
# 단어가 만들어지는 과정에 있는 단어들을 담을 세트와 단어의 점수를 담을 딕셔너리를 만들어줍니다.
for _ in range(w):
    word = input()
    for i in range(len(word)):
        if i == len(word) - 1:
            keep_going.add(word)
            if len(word) < 3:
                wants[word] = 0
            elif len(word) < 5:
                wants[word] = 1
            elif len(word) == 5:
                wants[word] = 2
            elif len(word) == 6:
                wants[word] = 3
            elif len(word) == 7:
                wants[word] = 5
            else:
                wants[word] = 11
            # 단어가 완성되었다면 점수를 밸류값으로 딕셔너리에 담아줍니다.
        else:
            keep_going.add(word[:i + 1])
            # 단어를 순회하며 각 자리까지를 세트형에 담아줍니다.

jump = input()
# 원하는 단어와 보드의 입력 사이에 들어오는 공백을 받아줍니다.
t = int(input())
# 테스트케이스를 받아줍니다.

def check(x, y, word):
# 보드를 이동하며 단어를 찾는 함수입니다
    global result
    dx = [1, 1, 1, 0, -1, -1, -1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    # 8방향탐색을 하여 단어를 찾아줍니다.
    if len(word) > 7:
        return
    # 단어의 길이는 최대 8글자이므로 8글자가 넘어가면 더 확인할 필요가 없습니다
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            # 8방향 탐색을 통해 이동했을때 보드 밖으로 나가지않는지 확인해줍니다.
            new = word + board[nx][ny]
            # 추가되는 문자를 이어붙인 단어를 정의해줍니다.
            if visited[nx][ny] == False and new in keep_going:
                # 이동할 위치가 사용한적 없는 칸이고 찾는 단어의 과정에 있는지 확인해줍니다.
                if new in wants:
                    find.add(new)
                    # 원하는 단어를 찾았다면 찾은 단어 목록에 추가해줍니다.
                visited[nx][ny] = True
                check(nx, ny, new)
                visited[nx][ny] = False
                # 보드칸을 사용 표시하고 재귀를 실행해준 뒤 사용 표시를 취소해줍니다.

for tc in range(t):
    result = 0
    # 최종 점수를 담을 변수를 설정해줍니다.
    board = [input() for _ in range(4)]
    # 주어지는 보드를 입력받아줍니다.
    visited = [[False for _ in range(4)] for _ in range(4)]
    find = set()
    # 보드의 칸을 사용했는지 확인할 방문처리 리스트를 만들고 원하는 단어가 만들어지면 담아둘 세트를 만듭니다.
    answer = ''
    # 최장 단어를 담을 변수를 설정해줍니다.

    for i in range(4):
        for j in range(4):
            if board[i][j] in keep_going:
                visited[i][j] = True
                check(i, j, board[i][j])
                visited[i][j] = False
    # 보드의 각 칸에서 원하는 문자가 만들어지는지 확인하는 함수를 실행시켜줍니다.
    find = sorted(list(find))
    # 세트형 구주에 담아둔 찾은 단어를 리스트형으로 바꾼다음 사전순으로 정렬해줍니다.
    for i in find:
        result += wants[i]
        if len(i) > len(answer):
            answer = i
    # 찾은 단어를 순회하며 단어로 얻을 점수를 더해주고 길이가 더 길다면 최장단어를 갱신해줍니다.
    if tc != t - 1:
        jump = input()
    # 테스트케이스 사이의 공백을 받아줍니다.
    print(result, answer, len(find))
    # 주어진 형식에 맞추어 출력을 실행해줍니다.