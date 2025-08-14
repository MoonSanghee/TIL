change = {'@':'a', '[':'c', '!':'i', ';':'j', '^':'n', '0':'o', '7':'t'}
n = int(input())
# w와 v 이외의 바꿔 사용한 문자들을 딕셔너리에 담고 주어지는 단어의 개수를 받아줍니다
for _ in range(n):
    word = input()
    result = ''
    cnt = 0
    # 주어지는 단어를 받고 원래 단어와 바꾼 문자의 개수를 담을 변수를 설정해줍니다
    for i in word:
        if i in change:
            result += change[i]
            cnt += 1
        else:
            result += i
    # 단어속 문자가 딕셔너리에 있다면 변환한 결과를 결과에 담고 변환한 문자의 수를 세어줍니다
    if "\\\\'" in word:
        cnt += result.count("\\\\'")
        result = result.replace("\\\\'", 'w')
        
    if "\\'" in word:
        cnt += result.count("\\'")
        result = result.replace("\\'", 'v')
    # w와 v의 개수를 세어줍니다.
    # w의 변형인 \\'에 v의 변형인 \'이 포함되므로 w,v 순서로 변환하여줍니다
    if cnt < (len(result)) / 2:
        print(result)
    else:
        print("I don't understand")
    # 바꾼 문자의 개수가 단어 길이의 반이 넘는지 확인하여 결과를 출력해줍니다