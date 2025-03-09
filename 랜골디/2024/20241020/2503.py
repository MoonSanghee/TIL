from copy import deepcopy

n = int(input())
# 주어지는 조합의 수를 받아줍니다
maybe = []
# 만들수 있는 조합을 모두 담을 리스트를 만들고 세 수를 이용하여 만든 모든 조합을 담아줍니다.
com = []
for i in range(1, 10):
    com.append(str(i))
    for j in range(1, 10):
        if str(j) not in com:
            com.append(str(j))
            for k in range(1, 10):
                if str(k) not in com:
                    com.append(str(k))
                    maybe.append(deepcopy(com))
                    com.pop()
            com.pop()
    com.pop()

for _ in range(n):
    call, s, b = input().split()
    call = list(call)
    s, b = int(s), int(b)
    # 주어지는 수와 스트라이크, 볼을 받아줍니다.
    
    new = []
    # 주어진 조건으로 확인한 만들수 있는 조합을 담을 변수를 설정해줍니다
    for com in maybe:
        check = [0, 0]
        for i in range(3):
            if com[i] == call[i]:
                check[0] += 1
            elif com[i] in call:
                check[1] += 1
        # 스트라이크와 볼을 확인하여 기록해줍니다
        if check[0] == s and check[1] == b:
            new.append(com)
        # 주어진 스트라이크, 볼과 같다면 new 리스트에 조합을 추가해줍니다
    maybe = new
    # 가능한 조합의 경우를 갱신해줍니다.

print(len(maybe))
# 남은 만들어질수 있는 조합의 수를 출력해줍니다.