n = int(input())
# 팀명 후보의 개수를 받아줍니다
for _ in range(n):
    word = input()
    low = 0
    high = 0
    # 팀명 후보를 받고 소문자와 대문자 개수를 담을 변수를 설정해줍니다
    if len(word) > 10:
        continue
    # 단어가 10보다 크면 성립하지 않습니다
    else:
        for i in range(len(word)):
            if word[i].isupper():
                high += 1
            elif word[i].islower():
                low += 1
        # 대소문자의 개수를 확인해줍니다
        if low >= high and (low != 0 or '-' in word):
            print(word)
        # 숫자이외의 문자를 포함하고 소문자가 대문자보다 작지않은 경우를 찾아 단어를 출력해줍니다