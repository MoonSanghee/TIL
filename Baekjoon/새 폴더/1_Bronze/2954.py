sentence = input()
# 암호가 포함된 문장을 받아줍니다
result = ''
# 원래 문장을 담을 변수를 설정해줍니다
idx = 0
# 확인할 문장의 위치를 담을 변수를 설정해줍니다
while idx < len(sentence):
    result += sentence[idx]
    # 확인할 위치의 문자를 원래 문장에 추가해줍니다
    if sentence[idx] in 'aeiou':
        idx += 3
    else:
        idx += 1
    # 나오는 문자가 aeiou에 포함된다면 뒤에 p와 자신 2개의 문자가 추가되어있으므로 idx를 3칸 뒤로 아니라면 1칸 뒤로 이동해줍니다
print(result)
# 원래 문장을 출력해줍니다