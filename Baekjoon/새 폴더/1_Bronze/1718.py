s = list(input())
key = list(input())
# 암화화할 문장과 키문장을 받아줍니다
for i in range(len(s)):
    if 97 <= ord(s[i]) <= 122:
        s[i] = chr(((ord(s[i]) - ord(key[i%len(key)]) - 1) % 26) + 97)
# 암호화를 진행하여줍니다
print("".join(s))
# 결과를 출력하여줍니다