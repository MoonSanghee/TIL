def solution(arr):
    answer = [0, 0]
    # 0과 1을 0개로 설정해줍니다.
    def check(x, y, size):
        # 확인할 좌표와 영역의 크기를 받아줍니다.
        s = arr[x][y]
        # 압축을 실행할 수 있는지 확인하기위해 기준이 되는 좌표를 확인해줍니다.
        for i in range(size):
            for j in range(size):
                if arr[x + i][y + j] != s:
                    # x, y부터 주어진 범위안에 모든 영역이 같은 값이 아니라면
                    size //= 2
                    # size를 반으로 줄이고
                    check(x, y, size)
                    check(x + size, y, size)
                    check(x, y + size, size)
                    check(x + size, y + size, size)
                    return
                    # 4분할하여 check를 재귀해주고 return합니다.
        answer[s] += 1
        # 모든 영역의 값이 일치한다면 어떤 값으로 압축되었는지 확인하여 answer에 추가하여줍니다.
    check(0, 0, len(arr))
    # x, y 좌표 0, 0을 기준으로 arr의 인덱스를 사이즈로 가지도록 함수를 실행기켜줍니다.
    return answer
    
