word = input()
# 주어지는 단어를 받아줍니다
for i in range(len(word)):
    new = word + word[:i][::-1]
    if new == new[::-1]:
        print(len(new))
        break
    # 주어지는 단어에서 앞에서 어디까지 자른 것을 이어주었을때 팰린드롬이 되는지 확인하여 가장 짧은 팰린드롬의 길이를 출력해줍니다