want = int(input())
# 이동하고자하는 채널의 번호를 받아줍니다
broken = int(input())
# 고장난 버튼의 수를 받아줍니다.
if broken:
    block = list(map(int, input().split()))
else:
    block = []
# 고장난 버튼이 있다면 고장난 버튼들을 받아줍니다.
now = 100
result = abs(now - want)
# 현재 번호에서 이동하는데 필요한 클릭수를 받아줍니다.

def click(number, cnt):
    global result
    if cnt == 7:
        return
    # 숫자 버튼을 7번 눌러 만들어지는 최소수인 1,000,000도
    # 원하는 채널의 범위중 가장 큰 500,000에 도달하는데 현재 위치한 100에서 움직이는데 필요한
    # 클릭수보다 많아지므로 클릭한 숫자 버튼이 7개면 계속 확인할 필요가 없습니다.
    for i in range(10):
        if broken != 0:
            if i in block:
                continue
            # 고장난 버튼이 존재하고 현재 누르려는 버튼이 고장난 버튼이라면 도착하지 
            # 못하므로 다음 버튼으로 넘어갑니다
        new = number * 10 + i
        # 지금 버튼을 눌러 도착하는 채널을 확인해줍니다.
        if abs(want - new) + 1 + cnt < result:
            result = abs(want - new) + 1 + cnt
            # 지금 버튼을 눌러 확인한 이동수를 최소 이동수와 비교하여 갱신해줍니다.
        click(new, cnt + 1)
        # 도착한 채널과 누른 버튼수를 넣어 함수를 실행해줍니다.

for i in range(10):
    if i not in block:
        click(i, 1)
        result = min(result, abs(want - i) + 1)
    # 이동가능한 모든 한자리 채널을 돌아가며 함수를 실행해줍니다.
print(result)
# 결과를 출력해줍니다.