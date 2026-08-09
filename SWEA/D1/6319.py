word = input()
new = word[::-1]
print(new)
if word == new:
    print("입력하신 단어는 회문(Palindrome)입니다.")