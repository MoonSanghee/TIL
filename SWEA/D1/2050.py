d = dict()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(26):
    d[alphabet[i]] = str(i + 1)
# 알파벳에 숫자를 맞춰줍니다
result = []
# 결과를 담을 변수를 설정해줍니다
word = input()
for i in word:
    result.append(d[i])
# 각 알파벳을 숫자로 교환해 리스트에 담아줍니다
print(' '.join(result))
# 결과를 주어진 형식대로 출력해줍니다