while True:
    n = int(input())

    if not n:
        break
    # 단어가 0개이면 반복을 그만둡니다.
    else:
        words = []

        for _ in range(n):
            word = input()
            words.append(word)
        # 단어가 있다면 words라는 리스트에 입력받은 단어들을 넣어주고
        words.sort(key=lambda word: word.lower())
        # 리스트를 word를 소문자로 변환한 기준으로 정렬하여줍니다.(대문자로 변환해도 됨)
        print(words[0])
        # 처음에 오는 단어를 출력해줍니다.