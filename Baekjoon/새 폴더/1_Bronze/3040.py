from itertools import combinations

dwarf = []
for i in range(9):
    dwarf.append(int(input()))
# 9명의 난쟁이를 받아줍니다.
com = combinations(dwarf, 7)
# 콤비네이션 함수를 이용하여 7명의 조합을 만들어줍니다.
for i in com:
    if sum(i) == 100:
        # 조합의 합이 100인 경우를 찾아
        for j in i:
            print(j)
            # 포함된 난쟁이들을 출력해줍니다.
        break