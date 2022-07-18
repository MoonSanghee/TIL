# Q. 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

# Output
# 3

# A.
# if char == "a" or "e" or "i" or "o" or "u":와 같이 표현하면
# char는 a와 같은지는 비교하지만, or 뒤의 'e'라는 표현은 불린 연산자로 이해하고
# 참이기에 모든 입력값에 count 값을 1씩 추가하게 된다.
# 따라서 char == "a" or orchar == "e" or orchar == "i" or orchar == "o" or orchar == "u"
# 처럼 모든 값의 연산을 넣어주거나 char in ('a', 'e', 'i', 'o', 'u')처럼 확인할 값들이
# 전부 들어간 순환 구조 속에 포함되는지 묻는 형태로 바꾸어주면 원하는 값을 얻을 수 있다.
word = "HappyHacking"

count = 0

for char in word:
    if char in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print(count)