n = int(input())
line = input()
# 주어지는 문자열의 길이와 문자열을 받아줍니다.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = 0
for i in alphabet:
    result = max(result, line.count(i))
# 알파벳을 순회하며 가장 많은 알파벳이 몇번 나오는지 찾아줍니다.

print(result)
# 결과를 출력해줍니다.