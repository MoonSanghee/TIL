n = int(input())
numbers = []
# 입력받을 내용의 수와 수를 담을 리스트를 만들어줍니다.
for _ in range(n):
    word = input()
    num = ''
    # 주어진 내용과 수를 담을 변수를 만들어줍니다.
    i = 0
    while i < len(word):
        if word[i] not in '1234567890':
            if num != '':
                numbers.append(int(num))
                num = ''
            # 정수가 아닌 문자가 나왔을때 담긴 num에 값이 있다면 리스트에 정수형으로 넣어줍니다.
        else:
            num += word[i]
            # 수가 나왔다면 문자열 형태로 num에 추가해줍니다.
        i += 1
        # 확인을 마쳤다면 인덱스 자리를 한 자리 미뤄줍니다.
    if num != '':
        numbers.append(int(num))
        # 모든 내용을 확인하고 num값이 존재한다면 정수형으로 리스트에 넣어줍니다.

numbers.sort()
for number in numbers:
    print(number)
    # 찾은 수를 오름차순으로 정렬하여 차례대로 출력해줍니다.