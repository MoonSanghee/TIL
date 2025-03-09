s = input()
t = input()
# 두 문자열을 받아줍니다.
ns = s
nt = t
# 함수를 실행시킨 결과물을 확인할 문자열을 만들어줍니다.
while len(ns) != len(nt):
    if len(ns) > len(nt):
        nt += t
    elif len(nt) > len(ns):
        ns += s
# 두 결과물의 길이가 같아질때까지 함수를 실행하여줍니다.
if ns == nt:
    print(1)
else:
    print(0)
# 실행 결과 두 함수의 결과물이 같다면 1 다르다면 0을 출력해줍니다.