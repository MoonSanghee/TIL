def check(sign, name):
    l = len(name)
    n = len(sign)
    # 간판과 편의점의 이름의 길이를 받아줍니다
    for d in range(1, (n - 1) // (l - 1) + 1):
        for i in range(n):
            if i + d * (l - 1) >= n:
                continue
            # 간판의 간격에 따라 확인하며 간판의 길이를 벗어나면 다음 차례를 확인합니다
            flag = True
            for k in range(l):
                if sign[i + k * d] != name[k]:
                    flag = False
                    break
                # 간판의 확인하는 위치의 글자가 편의점에 사용할 문자와 다르다면 확인을 멈추어줍니다
            if flag:
                return True
            # 편의점의 간판으로 사용 가능하다면 True값을 리턴해줍니다
    return False

n = int(input())
store_name = input()
result = 0
# 남아있는 간판의 개수와 새로 연 편의점의 이름을 받고 사용할 수 있는 간판의 수를 담을 변수를 만들어줍니다
for _ in range(n):
    old_sign = input()
    if check(old_sign, store_name):
        result += 1
    # 간판들을 확인하며 사용할 수 있는지에 따라 결과를 갱신해줍니다

print(result)
# 결과값을 출력해줍니다