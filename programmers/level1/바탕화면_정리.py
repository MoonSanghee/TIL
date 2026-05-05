def solution(wallpaper):
    answer = [len(wallpaper), len(wallpaper[0]), 0, 0]
    # 정답을 담을 리스트에 주어진 영역의 크기를 담아줍니다
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                answer[0] = min(answer[0], i)
                answer[1] = min(answer[1], j)
                answer[2] = max(answer[2], i + 1)
                answer[3] = max(answer[3], j + 1)
            # 파일이 있는 위치라면 영역을 갱신해야하는지 확인해줍니다
    return answer
    # 결과를 출력해줍니다