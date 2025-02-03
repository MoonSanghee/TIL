s = input()
k = input()
new = []
# 두 단어를 받고 숫자를 빼서 새로 만들 단어를 담을 변수를 설정해줍니다
for i in s:
    if i not in '1234567890':
        new.append(i)
# 숫자가 아닌 문자만 담아줍니다
if k in ''.join(new):
    print(1)
else:
    print(0)
    # 새로 만들어진 단어에 찾는 단어가 있는지 확인하여 결과를 출력해줍니다