n, m = map(int, input().split())
maps = []
# 그림의 크기와 그림을 담을 빈 리스트를 담아줍니다.
for i in range(n):
    temp = list(input())
    for j in range(m//2):
        if temp[j] != '.':
            temp[m - j - 1] = temp[j]
        elif temp[m - j - 1] != '.':
            temp[j] = temp[m - j - 1]
    maps.append(temp)
    # 그림의 각 줄을 확인하며 공백이 아니라면 접었을때 맞이하는 지점을 색칠해줍니다.
 
for i in range(len(maps)):
    print(''.join(maps[i]))
    # 각 줄을 여백없이 문자열로 묶어 출력해줍니다.