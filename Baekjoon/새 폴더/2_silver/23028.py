n, a, b = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(10)]
# 이수학 학기와 학점 22년 1학기부터 개설되는 과목수를 받아줍니다.
if a >= 66 and b >= 130:
    print('Nice')
    # 이미 졸업 조건을 충족했다면 "Nice"를 출력해줍니다
else:
    for i in range(8 - n):
        # n학기를 이수했으므로 8학기에서 남은 학기를 확인해줍니다.
        a += li[i][0] * 3
        b += li[i][0] * 3
        score = 6 - li[i][0]
        # 과목당 최대 6과목이 개설되므로 전공을 우선 최대한 수강해줍니다.
        if score < li[i][1]:
            b += score * 3
        else:
            b += li[i][1] * 3
        # 남은 학점으로 수강할수있는 최대 학점을 수강해줍니다.
    if a >= 66 and b >= 130:
        print('Nice')
    else:
        print('Nae ga wae')
        # 졸업 조건을 충족했는지 확인하고 결과를 출력해줍니다.