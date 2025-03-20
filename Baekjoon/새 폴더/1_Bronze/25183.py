n = int(input())
s = input()
cnt = 1
# 주어지는 문자열의 길이와 문자열을 받고 연속하는 문자열의 길이를 담을 변수를 설정해줍니다
for i in range(n - 1):
    if abs(ord(s[i]) - ord(s[i + 1])) == 1:cnt += 1
    else:cnt = 1
    if cnt == 5:break
    # 문자열이 연속한다면 1을 증가시키고 아니면 리셋시켜 당첨을 확인해줍니다
if cnt == 5:print('YES')
else:print('NO')
# 당첨을 확인한 결과를 출력시켜줍니다