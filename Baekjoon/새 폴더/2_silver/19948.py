poem = input()
title = ''.join(word[0].upper() for word in poem.split())
poem += title + '.'
# 시를 받고 제목을 구한 다음 제목과 시를 입력할수 있는지 확인하기위해 둘을 더해줍니다.
# 연속한 값은 길게 눌러서 입력하므로 연속한지 확인해줄것이기에 마지막에 주어지지않는 특수문자를 하나 추가해줍니다.
space = int(input())
count = list(map(int, input().split()))
d = {}
d[' '] = space
for i in range(len(count)):
    d[chr(97 + i)] = count[i]
# 띄워쓰기와 각 문자가 몇 개 존재하는지 받아줍니다.
for i in range(len(poem) - 1):
    if poem[i] == poem[i + 1]:
        continue
    # 연속하게 같은 문자가 온다면 횟수 차감을 하지않습니다.
    letter = poem[i]
    if letter.isupper():
        letter = letter.lower()
    if d[letter]:
        d[letter] -= 1
    else:
        print(-1)
        break
    # 키보드의 수명을 확인해 버튼을 아직 누를수있다면 횟수를 차감하고
    # 수명이 다했다면 -1을 출력하고 멈추어줍니다.
else:
    print(title)
    # 멈추지 않았다면 모든 입력이 가능하므로  제목을 출력해줍니다.