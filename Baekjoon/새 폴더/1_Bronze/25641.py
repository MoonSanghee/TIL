n = int(input())
N = input()
# 단어의 길이와 단어를 받아줍니다
s = N.count('s')
# s의 개수를 확인해줍니다
for i in range(n):
    if n - i == s * 2:
        print(N[i:])
        break
    # 단어가 균형을 이루는지 확인해줍니다
    elif N[i] == 's':
        s -= 1
    # 단어가 균형을 이루지않는다면 맨 앞의 단어를 빼줍니다