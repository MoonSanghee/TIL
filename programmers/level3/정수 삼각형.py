def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        # 첫 번째 줄은 더할 값이 없으므로 2번째 줄부터 순회합니다.
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
                # 아래줄의 가장 첫 번째 수의 경우 윗 줄의 첫 번재 값만 접하므로 
                # 윗 줄의 첫 번째 수를 더해주고
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
                # 아래줄의 마지막 수의 경우 위줄에서 마지막 값만 접하므로
                # 위 줄의 마지막 수만 더해줍니다.
                # 위의 줄의 길이가 아래 줄보다 1만큼 짧으므로 위 줄의 인덱스에서 1을 뺀 값을 더해줍니다. 
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
                # 그 외의 경우 왼쪽 위에 접한 수와 오른쪽 위에 접한 수중에 큰 수를 더하는데
                # 왼쪽의 수는 1만큼 작은 인덱스에 위치하고있고 오른쪽 수는 같은 인덱스에 위치하고 있습니다. 
            
    return max(triangle[-1])
    # 마지막 줄에서 가장 큰 값을 출력해줍니다.