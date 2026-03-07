n = int(input())
word = input()
# 주어지는 문자의 길이와 문자를 받아줍니다
result = [''] * n
# 결과를 리스트 형태로 받아줍니다
for i in range(n):
    if word[i] == '?':
        if word[n - 1 - i] == '?':
            result[i] = 'a'
        else:
            result[i] = word[n - 1 - i]
    else:
        result[i] = word[i]
# 각 자리의 문자를 확인하여 팰린드롬이 되도록 결과를 만들어줍니다
print(''.join(result))
# 만들어진 결과를 출력해줍니다