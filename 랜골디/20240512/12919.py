start = input()
end = input()
flag = 0
# 시작과 목표 단어를 받고 완성할수 있는지 담을 변수를 설정해줍니다.
def next(word, target):
    global flag
    if len(word) == len(target):
        if word == target:
            flag = 1
        return
    # 실행해서 만들어진 결과의 길이가 찾는 단어의 길이와 같다면 찾던 단어가 되었는지 확인해주고 함수를 멈추어줍니다.
    if target[-1] == 'A':
        next(word, target[:-1])
    # 마지막 문자가 A라면 A를 뺀 단어로 재귀해줍니다.
    if target[0] == 'B':
        next(word, target[:0:-1])
    # 첫 문자가 B라면 B를빼고 뒤집은 단어로 재귀해줍니다.
next(start, end)

print(flag)
# 함수를 실행하고 결과를 출력해줍니다.