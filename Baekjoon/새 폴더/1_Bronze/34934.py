n = int(input())
# 주어지는 학과의 수를 받아줍니다
for _ in range(n):
    name, year = input().split()
    if year == '2026':
        print(name)
    # 개설년도는 2001부터 2026년까지이지만 2026년에 개설된 유일한 과목이 존재한다고 하였으므로 2026년에 개설한 과목을 찾아 출력해줍니다