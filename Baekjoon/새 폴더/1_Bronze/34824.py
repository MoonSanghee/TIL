n = int(input())
names = [input() for _ in range(n)]
# 대회에 참가한 대학의 수와 순위를 받아줍니다
for name in names:
    if name == 'korea':
        print('Yonsei Lost...')
        break
    elif name == 'yonsei':
        print('Yonsei Won!')
        break
# 결과를 출력해줍니다