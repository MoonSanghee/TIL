n = int(input())
record = [input() for _ in range(n)]
m = int(input())
words = [input() for _ in range(m)]
# 끝말잊기를 진행한 기록과 빠진 단어 후보를 받아줍니다
if n == 1:
    print(words[0])
# 끝말잊기 문자가 1개라면 보기 단어중 첫번째 단어를 출력해줍니다
elif record[0] == "?":
    for word in words:
        if word not in record and word[-1] == record[1][0]:
            print(word)
            break
# 끝말잊기가 2단어 이상 진행되었고 모르는 단어가 첫 단어라면 보기의 단어가 사용된적 없고 마지막 문자가 다음 단어의 첫 문자와 같은것을 출력해줍니다.
elif record[-1] == "?":
    for word in words:
        if word not in record and word[0] == record[-2][-1]:
            print(word)
            break
# 끝말잊기가 2단어 이상 진행되었고 모르는 단어가 마지막 단어라면 보기의 단어가 사용된적 없고 첫 문자가 다음 단어의 마지막 문자와 같은것을 출력해줍니다
else:
    idx = record.index("?")
    for word in words:
        if word not in record and word[0] == record[idx - 1][-1] and word[-1] == record[idx + 1][0]:
            print(word)
            break
# 모르는 문자가 중간에 끼인 단어라면 이전 단어의 마지막 문자와 다음 단어의 첫 문자를 비교하고 사용된적 없는 단어를 찾아 출력해줍니다