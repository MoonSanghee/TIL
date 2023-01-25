n = int(input())
word = list(input())
# 처음 입력받는 단어를 기준으로 잡아주고
for i in range(1, n):
    word2 = list(input())
    for j in range(len(word)):
        if word[j] != word2[j]:
            word[j] = '?'
            # n - 1번만큼 단어를 더 입력 받아 모든 인덱스 자릿값을 비교하여 값이 다르면
            # word의 인덱스값을 '?'로 바꾸어줍니다.
print(''.join(word))
# word를 간격 없이 합쳐 출력해줍니다.