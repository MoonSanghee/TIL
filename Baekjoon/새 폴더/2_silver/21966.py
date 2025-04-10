N = int(input())
S = input()
# 문장의 길이와 주어지는 문장을 받아줍니다
if len(S) <= 25:
    print(S)
    # 문장이 충분히 짧다면 주어진 문장을 그대로 출력해줍니다
else:
    word = S[11:-11]
    # 생략할 부분을 받아줍니다
    result = ''
    if '.' not in word[:-1]:
        result = S[:11] + '...' + S[-11:]
    else:
        result = S[:9] + '......' + S[-10:]
    # 생략할 부분이 한 문장인지 확인하고 주어진 방식대로 수정해줍니다
    print(result)
    # 결과를 출력해줍니다