n = int(input())

problems = input()
# 문자열의 길이와 문자열을 받아줍니다.
R = []
B = []
paint = ''
paintb = ''
if problems[0] == 'R':
    B.append('')
else:
    R.append('')
# R문자 뭉치와 B 문자 뭉치를 담을 리스트를 만들고 시작 부분이 다른 색이라면 칠했음을 표시해줄 값을 넣어줍니다.
for i in range(n):
    if problems[i] == 'R':
        paint += problems[i]
        if paintb:
            B.append(paintb)
            paintb = ''
    else:
        paintb += problems[i]
        if paint:
            R.append(paint)
            paint = ''
if paint:
    R.append(paint)
elif paintb:
    B.append(paintb)
# 문자열을 칠하는 것을 확인해 리스트에 뭉치를 넣어줍니다.
if problems[-1] == 'R':
    B.append('')
else:
    R.append('')
# 마지막 배경 이 칠해졌는지 확인하여 칠하여줍니다.
cnt = min(len(R), len(B))
print(cnt)
# R과 B 리스트 길이를 비교하여 작은 값을 출력해줍니다.