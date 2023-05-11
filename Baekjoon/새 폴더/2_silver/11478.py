word = input()
n = len(word)
# 단어를 입력받고 단어의 길이를 구해줍니다.
s = set()
# 부분 문자열을 넣어줄 세트를 만들어줍니다.
for i in range(n):
    for j in range(n - i):
        s.add(word[j: j + i + 1])
        # 단어의 길이 이하의 모든 부분 문자열을 set형 자료구조에 넣어줍니다.

print(len(s))
# s의 길이를 출력해줍니다.