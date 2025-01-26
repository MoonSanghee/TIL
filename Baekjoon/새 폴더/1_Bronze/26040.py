A = input()
B = list(input().split())
# 기본 문자열과 소문자로 바꿀 대문자들을 받아줍니다
for i in B:
    A = A.replace(i, i.lower())
# 바꿀 문자를 소문자로 바꿔줍니다
print(A)
# 결과를 출력해줍니다