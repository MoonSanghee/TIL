special = "!@#$%^&*()-+"
number = "0123456789"
small = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
check = [number, small, capital, special]
# 4그룹의 필수 입력을 받아줍니다
cnt = 0
# 포함되지않은 그룹의 수를 담을 변수를 설정해줍니다
n = int(input())
S = input()
# 문자열의 길이와 문자열을 받아줍니다
for i in range(4):
    for j in S:
        if j in check[i]:
            break
    else:
        cnt += 1
    # 각 그룹의 값이 포함되었는지 확인하고 포함되지 않았다면 추가할 그룹의 수를 갱신하여줍니다
print(max(6-n, cnt))
# 최소 길이를 충족하기위해 필요한 문자열의 수와 필요한 그룹의 종류를 비교하여 큰쪽을 출력해줍니다