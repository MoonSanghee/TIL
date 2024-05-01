while True:
    word = input()
    if word == '#':
        break
    # '#'이 들어올때까지 입력을 받아줍니다.
    no = True
    for i in 'aeiou':
        if i in word:
            no = False
    # 모음을 가지고있는지 확인해줍니다.
    if no:
        print(word + 'ay')
        # 모음이 없다면 단어에 ay를 붙여 출력합니다.
    else:
        for i in range(len(word)):
            if word[i] in 'aeiou':
                print(word[i:] + word[:i] + 'ay')
                break
        # 모음이 있다면 모음이 처음 나오는 차례를 확인하여 모음이 나온 이전을 
        # 모음이 나온 이후부터 끝까지의 뒤로 보내고 ay를 붙여 출력해줍니다.