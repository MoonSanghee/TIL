word = str(input())
words = []

for _ in word:
    words.append(word)
    word = word[1:]

for i in sorted(words):
    print(i)

# 1글자가 될때까지 인덱스부터 마지막까지의 문자열을 빈 리스트에 넣고 리스트를 정렬하고 차례로 출력해주었습니다.