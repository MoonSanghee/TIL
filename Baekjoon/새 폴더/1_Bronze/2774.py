t = int(input())
# 수의 개수를 받아줍니다.
for _ in range(t):
    n = set(list(input()))
    # 수를 문자열 형태로 받아 리스트에 담아 각 자리를 나누고 set을 이용하여 중복되는 수를 걸러줍니다.
    print(len(n))
    # 몇개의 수로 이루어졌는지 출력해줍니다.