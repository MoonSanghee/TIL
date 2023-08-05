n = int(input())
# 단어의 개수를 받아줍니다.
base = input().split('*')
# 기준이 되는 단어의 시작과 끝부분을 나누어줍니다.
length = len(base[0]) + len(base[1])
# 시작과 끝의 길이 합을 구해줍니다.
for _ in range(n):
    word = input()
    # 주어질 단어들을 받아줍니다.
    if length > len(word):
        print('NE')
        # 기준보다 길이가 짧다면 패턴이 일치하지 않습니다.
    else:
        if base[0] == word[:len(base[0])] and base[1] == word[-len(base[1]):]:
            print('DA')
            # 단어의 시작과 끝이 기준의 시작과 끝과 같다면 패턴이 일치하고
        else:
            print('NE')
            # 아니라면 패턴이 일치하지 않는다고 출력해줍니다.