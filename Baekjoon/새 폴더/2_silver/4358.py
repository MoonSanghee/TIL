import sys
input = sys.stdin.readline

total = 0
# 나무의 수를 세어줍니다.
dictionary = dict()
# 딕셔너리를 만들어줍니다.
while True:
    word = input().strip()
    # 단어를 입력받아줍니다
    if word == '':
        break
    # 공백을 입력받으면 입력을 멈추어줍니다.
    total += 1
    # 나무를 1 더해줍니다.
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
    # 단어가 처음 나오면 1개 있다고 value를 맞추어주고
    # 나온적 있다면 value를 1 더해줍니다.
new = dict(sorted(dictionary.items()))
# 딕셔너리를 items를 기준으로 정렬하여 바꾸어줍니다.
for word in new:
    v = new[word]
    per = v / total * 100
    print(("%s %.4f" %(word, per)))
    # new를 순회하며 word기준으로 소수점 4번째짜리까지 반올림하여 출력해줍니다.