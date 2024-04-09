import sys

bees = dict()
works = ['Re','Pt','Cc','Ea','Tb','Cm','Ex']
for work in works:
    bees[work] = 0
cnt = 0
# 출력할 일의 순서대로 딕셔너리에 넣어 밸류를 0으로 설정해주고 전체 행동수를 담을 변수를 설정해줍니다.
lines = sys.stdin.readlines()
# 여러줄의 입력을 받아줍니다.
for line in lines:
    array = list(line.split())
    for i in array:
        if i in bees:
            bees[i] += 1
        cnt += 1
        # 작업이 확인하고자 하는 작업이라면 딕셔너리 밸류값을 1 증가시켜주고 전체 작업을 갱신해줍니다.

for i in works:
    print(i, bees[i], '{:.2f}'.format(bees[i] / cnt))

print(f'Total {cnt} 1.00')
# 작업을 순서대로 원하는 형식대로 출력하고 전체 작업도 주어진 형식대로 출력해줍니다.