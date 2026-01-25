n = int(input())
word = input()
# 주어지는 단어의 길이와 단어를 받아줍니다
d = dict()
for i in 'uospc':
    d[i] = 0
# 'uospc'에 필요한 문자가 몇개인지 확인하기위한 딕셔너리를 만들어줍니다
for i in word:
    if i in d:
        d[i] += 1
# 주어진 단어를 순회하며 필요한 문자라면 개수를 갱신해줍니다
result = n
for i in d:
    result = min(result, d[i])
# uospc에 중복되는 문자가 없으므로 딕셔너리를 순회하며 가장 적은 문자의 개수를 확인해줍니다
print(result)
# 결과를 출력해줍니다