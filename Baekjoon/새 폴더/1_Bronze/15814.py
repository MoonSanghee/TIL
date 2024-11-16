s = list(input())
t = int(input())
# 최초 주어지는 단어와 야바위를 실행하는 횟수를 받아줍니다
for _ in range(t):
    a, b = map(int, input().split())
    s[a],s[b] = s[b], s[a]
    # 야바위로 위치를 바꿀 문자의 위치를 받고 두 문자를 바꿔줍니다
print(''.join(s))
# 새로 만들어진 문자를 출력해줍니다