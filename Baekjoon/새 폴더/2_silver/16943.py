from itertools import permutations
# 순열 라이브러리를 불러옵니다
a, b = input().split()
b = int(b)
c = -1
# 두 수 a,b를 받고 b를 정수형으로 변환해주고 결과물을 담을 c를 설정해줍니다
numbers = [''.join(item) for item in permutations(a)]
# 순열을 순회하며 만들어진 수들을 리스트에 담아줍니다
for i in numbers:
    if i[0] == '0':
        continue
    i = int(i)
    if i < b:
        c = max(c, i)
    # 자릿수가 같은 수중에 b보다 작은 최대값을 구하여 c에 담아줍니다

print(c)
# 결과를 출력해줍니다