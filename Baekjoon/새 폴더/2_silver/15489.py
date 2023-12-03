r, c, w = map(int, input().split())
# r번째 줄 , c번 자리, 변의 길이 w를 받아줍니다.
tri = [[1]]
for i in range(r + w - 1):
    last = tri[-1]
    line = [1]
    for j in range(len(last) - 1):
        line.append(last[j] + last[j + 1])
    line.append(1)
    tri.append(line)
# r + w를 한 변의 길이로 가지는 파스칼 삼각형을 만들어줍니다.

result = 0
for i in range(w):
    for j in range(i + 1):
         result += tri[i + r - 1][c + j - 1]
# r번째 줄 c번째 수부터 삼각형 영역안의 값들을 result에 더해줍니다.
print(result)
# 삼각형 안의 모든 수를 더한 값을 출력해줍니다.