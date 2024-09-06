word = input()
# 단어를 받아줍니다.
result = []
# 만들수있는 모든 단어를 담을 리스트를 만들어줍니다.
for i in range(len(word)):
    for j in range(i + 1, len(word) - 1):
        # 단어를 3단어로 자르기위해 2지점을 선택해줍니다.
        first = word[:i + 1][::-1]
        second = word[i + 1:j + 1][::-1]
        third = word[j + 1:][::-1]
        new = first + second + third
        result.append(new)
        # 잘라서 만들어진 단어들을 뒤집어 새단어를 만들고 리스트에 넣어줍니다.

result.sort()
print(result[0])
# 단어가 들어가있는 리스트를 정렬해 첫 단어를 출력해줍니다.
