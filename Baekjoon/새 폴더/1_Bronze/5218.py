t = int(input())
alpha = dict()
number = 1
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    alpha[letter] = number
    number += 1
# 각 알파벳에 숫자를 매칭하여 딕셔너리에 저장하여줍니다.
for tc in range(t):
    word1, word2 = input().split()
    # 두 단어를 받아줍니다.
    result = 'Distances:'
    for i in range(len(word1)):
        if alpha[word2[i]] - alpha[word1[i]] >= 0:
            result += ' ' + str(alpha[word2[i]] - alpha[word1[i]])
        else:
            result += ' ' + str(26 + alpha[word2[i]] - alpha[word1[i]])
    # 두번째 오는 문자의 값이 클 경우 거리가 양수이므로 공백과 그 거리를 문자형으로 변환시켜 더해주고
    # 작을 경우 공백과 26에 거리 차만큼을 빼주어 더해줍니다.
    print(result)
    # result에 저장된 값을 출력해줍니다.