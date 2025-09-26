s = input()
t = input()
# 두 문자열을 받아줍니다
result = ''
for i in t:
    if i not in s:
        result += i
# s에 포함되지 않는 문자들만 골라줍니다
print(result)
# 결과를 출력해줍니다