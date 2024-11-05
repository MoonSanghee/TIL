word = input()
one = 'CIJLOSUVZ'
two = 'BDPQRTWXY'
# 단어를 입력받고 획수를 구별해줍니다.

result = []
for i in word:
    if i in one:
        result.append(1)
    elif i in two:
        result.append(2)
    else:
        result.append(3)
    # 단어의 각 문자 획수를 확인하여 리스트에 넣어줍니다.

while True:
    if len(result) == 1:
        if result[0] % 2:
            print("I'm a winner!")
        else:
            print("You're the winner?")
        break
    # 토너먼트를 진행하여 1개의 수만 남으면 결과를 출력해줍니다.
    new = []
    for i in range(len(result) // 2):
        new.append((result[i * 2] + result[i * 2 + 1]) % 10)
    if len(result) % 2:
        new.append(result[-1])
    result = new
    # 토너먼트를 진행하고 리스트를 갱신해줍니다.