n = int(input())
vote = input()
a, b = 0, 0

for i in vote:
    if i == 'A':
        a += 1
    else:
        b += 1
# A,B의 득표를 확인해줍니다.
if a >b:
    print('A')
elif b > a:
    print('B')
else:
    print('Tie')
# 결과를 출력해줍니다.