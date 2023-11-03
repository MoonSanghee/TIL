n = int(input())
answer = input()
# 문제의 수와 답을 차례로 받아줍니다.
Adrian = 0
Bruno = 0
Goran = 0
# Adrian, Bruno, Goran의 맞은 수를 확인할 변수를 생성해줍니다.

for i in range(n):
    if i % 3 == 0:
        if answer[i] == 'A':
            Adrian += 1
    elif i % 3 == 1:
        if answer[i] == 'B':
            Adrian += 1
    else:
        if answer[i] == 'C':
            Adrian += 1
    # Adrian의 정답을 비교해주서 맞았다면 맞은 수를 증가하여줍니다.
    
    if i % 4 == 0 or i % 4 == 2:
        if answer[i] == 'B':
            Bruno += 1
    elif i % 4 == 1:
        if answer[i] == 'A':
            Bruno += 1
    else:
        if answer[i] == 'C':
            Bruno += 1
    # Bruno의 정답을 비교해주서 맞았다면 맞은 수를 증가하여줍니다.
    
    if i % 6 == 0 or i % 6 == 1:
        if answer[i] == 'C':
            Goran += 1
    elif i % 6 == 2 or i % 6 == 3:
        if answer[i] == 'A':
            Goran += 1
    else:
        if answer[i] == 'B':
            Goran += 1
    # Goran의 정답을 비교해주서 맞았다면 맞은 수를 증가하여줍니다.

number = max(Adrian, Bruno, Goran)
print(number)
# 세명의 점수를 비교하여 최다 득점을 확인해줍니다.
if number == Adrian:
    print('Adrian')
if number == Bruno:
    print('Bruno')
if number == Goran:
    print('Goran')
# 최다점과 비교하여 최다점을 받은 사람의 닉네임을 출력해줍니다.