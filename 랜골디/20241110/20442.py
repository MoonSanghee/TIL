line = input()
# 주어지는 문자열을 받아줍니다.
l, r = 0, len(line) - 1
lk, rk = 0, 0
# 좌우 끝 좌표로 포인터 위치를 설정하고 좌우에 위치한 k의 개수를 담을 변수를 설정해줍니다.
Rs = line.count("R")
result = max(0, Rs)
used = 0
# R의 개수를 확인하여 최대 길이로 설정해주고 사용한 R의 개수를 담을 변수를 설정해줍니다.₩

while l < r:
    # l포인터가 r 포인터의 위치보다 오른쪽에 위치할수 없으므로 같은 자리에 위치하게되면 반복을 멈추어줍니다.
    if line[l] == 'R':
        used += 1
    else:
        lk += 1
    l += 1
    # l포인터의 자리값을 확인하여 R이라면 사용을 표시하고 K라면 lk값을 증가시켜줍니다.

    while lk != rk:
        if line[r] == "R":
            used += 1
        else:
            rk += 1
        r -= 1
    # lk와 rk의 값이 같을때까지 rk를 당겨줍니다.
    if used == Rs:
        break
    # R을 모두 사용하였다면 조건에 맞는 문자열을 만들수 없으므로 반복을 멈추어줍니다.
    result = max(result, Rs - used + lk + rk)
    # result 값을 갱신해줍니다

print(result)
# 최장 문자열의 길이를 출력해줍니다.