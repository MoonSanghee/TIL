word = list(input())
# 주어지는 단어를 받아줍니다
for i in range(len(word)):
    times = sum(list(map(int, list(str(ord(word[i]))))))
    print(word[i] * times)
    # 아스키 코드 값의 자릿수들을 더해 알파벳 개수를 구해 알파벳들을 출력해줍니다