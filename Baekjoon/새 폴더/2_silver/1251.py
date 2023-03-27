word = input()
made = []
# 단어를 입력받고 만들수 있는 단어들을 저장할 리스트를 만들어줍니다.
n = len(word)
for i in range(1, n - 1):
    # 자른 단어들의 최소 길이는 1이므로 처음 자르는 위치는 0번 인덱스 뒤부터 가능하고
    # 두 번째 자른 후 마지막 단어도 1이상의 길이를 가져야하므로 인덱스 1이상이 남아야합니다.
    for j in range(i + 1, n):
        new = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
        made.append(new)
        # 두 번 자른 후 나온 3개의 단어를 각각 뒤집은 다음 합쳐서 나온 단어를
        # made 리스트에 넣어줍니다.
made.sort()
print(made[0])
# made 리스트를 정렬시키고 0번 인덱스값을 출력해줍니다.