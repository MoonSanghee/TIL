s, k = input().split()
# 주어지는 변수들을 받아줍니다
used = []
cnt = 1
result = ''
# 사용한 문자와 연속한 길이 결과를 담을 변수를 설정해줍니다
for i in range(1,len(s)):
    if s[i].lower() != s[i - 1].lower():
        # 연속한 문자가 다르다면
        if s[i - 1].lower() in used:
            continue
        # 이전의 문자가 시용된적 있는지 확인해줍니다
        elif cnt >= int(k):
            result += '1'
        else:
            result += '0'
        # 사용한적 없다면 가준에 맞게 결과값을 갱신해줍니다
        cnt = 1
        used.append(s[i - 1].lower())
        # 길이값을 갱신해주고 사용한 문자를 추가해줍니다
    else:
        cnt += 1
        # 연속한 문자가 같다면 길이를 더해줍니다

if s[i].lower() not in used:
    if cnt >= int(k):
        result += '1'
    else:
        result += '0'
# 마지막 문자가 사용되었는지 확인하여 결과값을 더해줍니다
print(result)
# 결과를 출력해줍니다