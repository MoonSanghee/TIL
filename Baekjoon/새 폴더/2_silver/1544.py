words = set()
# 단어를 담을 셋을 만들어줍니다.
n = int(input())
# 주어지는 단어의 개수를 받아줍니다.
for _ in range(n):
    word = input()
    for i in range(len(word)):
        if word[i:] + word[:i] in words:
            break
    else:
        words.add(word)
    # 주어지는 단어를 입력받아 같은 단어가 나온적없으면 set에 추가해줍니다.

print(len(words))
# 몇개의 다른 단어가 주어졌는지 출력해줍니다.