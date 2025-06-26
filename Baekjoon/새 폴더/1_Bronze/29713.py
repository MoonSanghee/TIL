n = int(input())
word = input()
# 단어의 길이와 주어지는 알파벳 씰을 받아줍니다
d = dict()
for i in word:
    d[i] = d.get(i, 0) + 1
# 주어지는 씰의 알파벳 개수를 딕셔너리에 담아줍니다
result = n
# 만들고자하는 단어에 E와 R이 2개씩 나머지는 1개씩 필요하므로 문자들로 몇개씩 만들수있는지 확인해줍니다
result = min(result, d.get("E", 0) // 2)
result = min(result, d.get("R", 0) // 2)

for i in "BONZSILV":
    result = min(result, d.get(i, 0))

print(result)
# 결과를 출력해줍니다