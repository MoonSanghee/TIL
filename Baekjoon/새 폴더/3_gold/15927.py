word = input()
# 주어지는 단어를 받아줍니다
if word == word[0] * len(word):
    print(-1)
# 하나의 문자가 반복되는 단어라면 모든 부분문자열이 회문이므로 -1을 출력해줍니다
elif word == word[::-1]:
    print(len(word) - 1)
# 하나의 문자열로만 이루어지지는 않았지만 회문이라면 전체 길이에서 1을 뺀 값을 출력해줍니다
else:
    print(len(word))
# 아니라면 주어진 단어의 길이를 출력해줍니다