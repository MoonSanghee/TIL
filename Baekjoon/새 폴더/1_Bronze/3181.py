banned = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
words = list(input().split())
# 금지된 단어 목록을 받고 주어지는 단어들을 받아줍니다.
result = words[0][0].upper()
# 첫 단어의 첫 글자를 따 result에 담아줍니다.
for i in range(1, len(words)):
    word = words[i]
    if word not in banned:
        result += word[0].upper()
# 그 이후의 단어들을 순회하면서 무시하면 안 되는 단어라면 첫 글자를 따 result 붙여줍니다.
print(result)
# result 값을 출력해줍니다.