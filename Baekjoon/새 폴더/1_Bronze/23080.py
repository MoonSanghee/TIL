n = int(input())
word = input()
# 확인할 간격과 주어지는 암호를 받아줍니다.
result = ''
for i in range(0, len(word), n):
    result += word[i]
# n간격마다 문자를 result에 더해줍니다.
print(result)
# result에 완성된 단어를 출력해줍니다.