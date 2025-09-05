n = int(input())
# 단어의 수를 받아줍니다
for _ in range(n):
    word = input().lower()
    # 단어의 모든 문자를 소문자로 변환하여 받아줍니다
    if word == word[::-1]:
        print("Yes")
    else:
        print("No")
    # 펠린드롬이 성립하는지 출력하여줍니다