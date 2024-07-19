n = int(input())
# 단어의 개수를 받아줍니다.
result = []
# 단어를 담을 리스트를 만들어줍니다.
for _ in range(n):
    word = sorted(list(input()))
    # 입력받는 단어를 리스트에 담고 정렬해줍니다.
    if word not in result:
        result.append(word)
    # 정렬한 단어가 result에 없다면 추가해줍니다.
print(len(result))
# result에 담긴 단어의 개수를 출력해줍니다.