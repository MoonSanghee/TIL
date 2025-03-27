sh, sm = map(int, input().split())
eh, em = map(int, input().split())
n = input()
# 주어지는 변수들을 받아줍니다
result = 0
# 찾는 숫자가 있는지 확인하여 담을 변수를 설정해줍니다
while True:
    t = f"{sh:02}{sm:02}"
    if n in t:result += 1
    # 시작 시간을 문자열형태로 변환하여 찾는 수가 있는지 확인해줍니다
    if sm == em and sh == eh:
        break
    # 시작 시간이 목표 시간에 도달하면 멈추어줍니다
    sm += 1
    if sm == 60:
        sm = 0
        sh += 1
    # 시작 분을 1증가시키고 60을 넘겼다면 0으로 바꾸고 시간을 증가시켜줍니다
print(result)
# 결과를 출력해줍니다