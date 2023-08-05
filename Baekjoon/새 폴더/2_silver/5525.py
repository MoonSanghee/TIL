n = int(input())
m = int(input())
words = input()
# p의 길이와 주어진 단어의 길이, 단어를 입력받아줍니다.

cursor = 0
length = 0
count = 0
# 커서의 위치와 현재 확인한 단어의 길이 확인한 단어가 들어있는 횟수를 저장할
# 변수를 지정해줍니다.

while cursor < m - 1:
    # 커서가 단어 밖에 나갈때까지 반복을 계속합니다.
    if words[cursor: cursor + 3] == 'IOI':
        # 주어진 단어에서 커서 위치부터 3개의 낱말이 'IOI'의 형태를 가진다면
        length += 1
        # 길이를 1 늘려주고
        cursor += 2
        # 커서를 2칸 뒤로 보내줍니다.
        if length == n:
            count += 1
            length -= 1
            # 커서가 확인하는 단어만큼 길어졌다면
            # count를 1 늘려주고 길이를 1만큼 줄여줍니다.
    else:
        cursor += 1
        length = 0
        # 주어진 커서의 위치부터 3개의 낱말이 'IOI'의 형태가 아니라면
        # 커서를 한 칸 뒤로 보내고 길이를 0으로 만들어줍니다.

print(count)
# count에 저장된 단어가 나온 횟수를 출력해줍니다.