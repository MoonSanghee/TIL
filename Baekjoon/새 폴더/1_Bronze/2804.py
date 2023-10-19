word1, word2 = input().split()

for i in range(len(word1)):
    if word1[i] in word2:
        col = i
        row = word2.index(word1[i])
        break
# 두 단어의 공통된 문자를 찾아줍니다.
    
for i in range(len(word2)):
    if i == row:
        print(word1)
    else:
        print('.'*col + word2[i] + '.'*(len(word1)-col-1))
# 겹치는 문자의 줄은 word1을 아니라면 word2의 문자와 '.'으로 이루어진 문자열을 출력해줍니다.