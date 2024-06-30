key = input()
isError = False
# 입력되는 변수를 받고 제대로된 형식이 아닌지 확인할 변수를 설정해줍니다.
if key[0] == '_' or key[0].isupper() or key[-1] == '_':
    isError = True
# 변수의 첫 문자가 언더바(_) 혹은 대문자이거나 마지막 문자가 언더바(_)라면 에러라고 설정해줍니다
if '_' in key:
    words = list(key.split('_'))
    # 변수에 언더바(_)가 포함되어있다면 C++ 변수인지 확인해주기위해 언더바를 기준으로 단어를 분리해 리스트에 넣어줍니다.
    result = ''
    for i in words:
        if len(i) == 0:
            isError = True
            break
        # 구분된 단어의 길이가 0이라면 언더바가 연속한것이므로 에러처리해줍니다.
        for j in i:
            if j.isupper():
                isError = True
                break
        # 단어에 대문자가 포함되어있어도 에러처리를 해줍니다.
        if result:
            i = i.capitalize()
        result += i
        # 위 두 조건을 통과한다면 단어의 첫 문자를 대문자로 바꾸고 새 변수에 더해줍니다.
elif isError == False:
    # 자바 변수 확인입니다.
    result = ''
    for i in key:
        if i.isupper():
            result += '_'
            i = i.lower()
        result += i
    # 대문자가 나오면 언더바(_)를 추가하고 대문자를 소문자로 변환하여 추가해줍니다.

if isError:
    print('Error!')
else:
    print(result)
    # 에러인지 여부를 확인하고 결과를 출력해줍니다.