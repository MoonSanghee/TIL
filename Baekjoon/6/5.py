# 6-5 문제번호 1157

# Q. 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# A.
word = input().upper()
word_l = list(set(word))

c = []
for i in word_l:
    d = word.count(i)
    c.append(d)

if c.count(max(c)) > 1:
    print('?')
else:
    e = c.index(max(c))
    print(word_l[e])