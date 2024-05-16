result = ''
# 단어를 담을 변수를 설정해줍니다.
while True:
    line = list(input().split(' '))
    # 각 줄을 입력받고 공백을 기준으로 나눠 리스트에 담아줍니다.
    for word in line:
        new = ''
        for char in word:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or char == '-':
                new += char
        if len(new) > len(result):
            result =  new
        # 단어에 포함되는 문자인지 확인해 단어를 확인해주고 이전에 가지고있는 단어보다 길다면 갱신해줍니다.
    if line[-1] == 'E-N-D':
        break
    # 문장의 마지막 단어가 끝을 의미하는지 확인해줍니다.

print(result.lower())
# 단어를 소문자로 출력해줍니다.