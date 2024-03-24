book = input()
looking = input()
# 훼손된 교과서와 찾을 키워드를 받아줍니다.
new = ''
for i in book:
    if i not in '0123456789':
        new += i
# 교과서의 훼손된 부분을 뺀 나머지 부분을 구해줍니다.

if looking in new:
    print(1)
else:
    print(0)
# 찾는 부분이 존재하는지 확인하여 결과를 출력해줍니다.