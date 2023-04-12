t = int(input())
# 테스트 케이스를 받아줍니다.
for tc in range(t):
    n = int(input())
    # 의상의 가지 수를 받아줍니다.
    clothes = dict()
    # 의상을 딕셔너리 형태로 담아줍니다.
    for i in range(n):
        cloth, category = input().split()
        # 의상명과, 분류를 의상수만큼 받아
        if category in clothes:
            clothes[category].append(cloth)
            # 분류가 있다면 밸류값에 의상을 추가해주고
        else:
            clothes[category] = [cloth]
            # 없다면 의상을 리스트에 담긴 형태로 만들어줍니다.
    
    count = 1
    for i in clothes:
        count *= (len(clothes[i]) + 1)
    print(count - 1)
    # 모든 의상을 안 입는 경우를 제외하면 분류별로 모든 경우의 수를 기본 count (1)
    # 에 곱하고 모든 의상을 안 입은 상태를 빼준다는 의미로 마지막에 1을 빼줍니다.