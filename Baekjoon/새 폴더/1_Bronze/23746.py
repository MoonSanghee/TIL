n = int(input())
d = dict()
# 입력받을 압축한 문자의 수와 압축한 문자를 담을 딕셔너리를 만들어줍니다.
for _ in range(n):
    v, k = input().split()
    d[k] = v
    # 딕셔너리에 압축한 결과와 내용을 넣어줍니다.
word = ''
keywords = list(input())
for keyword in keywords:
    word += d[keyword]
# 압축 전의 문자열로 변환하여줍니다.
s, e = map(int, input().split())

print(word[s - 1: e])
# 원하는 구간을 출력하여줍니다.