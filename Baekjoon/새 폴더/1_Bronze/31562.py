n, m = map(int, input().split())
d = dict()
# 정보가 주어지는 곡의 수와 멜로디 수를 받고 곡의 정보를 담아둘 변수를 설정해줍니다
for _ in range(n):
    T, S, a1, a2, a3, a4, a5, a6, a7 = list(input().split())
    melody = (a1, a2, a3)
    # 곡의 정보를 받고 앞의 세음을 묶어줍니다
    if melody in d:
        d[melody] = '?'
    else:
        d[melody] = S
    # 처음 세 음이 나온적 있다면 중복되므로 노래를 찾을수 없기때문에 ?표로 값을 바꾸어주고 
    # 아니면 노래 제목을 값으로 매칭시켜줍니다

for _ in range(m):
    command = tuple(input().split())
    if command in d:
        print(d[command])
    else:
        print("!")
    # 입력을 받고 첫 세음의 정보가 있다면 저장된 값을 없다면 찾을수 없다는 값을 출력해줍니다