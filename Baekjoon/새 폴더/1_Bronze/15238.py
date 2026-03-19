n = int(input())
word = input()
d = dict()
# 단어의 길이와 단어를 받고 문자의 개수를 담을 딕셔너리를 만들어줍니다
for i in word:
    d[i] = d.get(i, 0) + 1
# 각 문자들이 몇개씩 있는지 딕셔너리에 담아줍니다
result = word[0]
# 단어에 포함되는 임의의 문자를 결과로 설정해줍니다
for i in d:
    if d[i] > d[result]:
        result = i
# 단어에 포함되는 문자중 가장 많이 사용된것을 찾아줍니다
print(result, d[result])
# 가장 많이 사용된 문자와 그 문자가 몇 번 사용되었는지 출력해줍니다