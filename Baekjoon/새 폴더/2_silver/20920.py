import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 단어의 수와 기준 길이를 받아줍니다.
d = dict()
# 딕셔너릴ㄹ 만들어줍니다.
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    # 단어의 길이를 확인하여 딕셔너리에 넣어줍니다.
wordList = sorted(d.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))
# 딕셔너리에 들어있는 단어들을 나온 빈도와 사전순으로 정렬하여줍니다.
for word in wordList:
    print(word[0])
# 정렬된 단어를 차례대로 출력해줍니다.