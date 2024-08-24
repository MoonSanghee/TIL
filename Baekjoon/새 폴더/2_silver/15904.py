line = input()
# 문장을 받아줍니다.
idx = 0
need = 'UCPC'
# 줄여서 만드려는 단어를 변수에 담고 필요한 문자를 확인할 변수도 설정해줍니다.
for i in line:
    if need[idx] == i:
        idx += 1
        if idx == 4:
            print("I love UCPC")
            break
    # 필요한 문자가 나왔다면 idx값을 한 자리 밀어주고 다 모았다면 원하는 결과를 출력해줍니다.
else:
    print("I hate UCPC")
# 단어를 만드는데 실패했다면 주어진 양식대로 출력해줍니다.