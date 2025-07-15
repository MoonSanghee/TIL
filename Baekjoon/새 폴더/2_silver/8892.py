t = int(input())
# 테스트 케이스의 개수를 받아줍니다
for tc in range(t):
    n = int(input())
    words = [input().strip() for _ in range(n)]
    # 주어지는 단어의 개수를 받고 주어지는 단어들을 받아줍니다
    flag = False
    # 펠린드롬이 만들어졌는지를 담을 변수를 설정해줍니다
    for i in range(n):
        for j in range(i + 1, n):
            made = words[i] + words[j]
            made2 = words[j] + words[i]
            if made == made[::-1]:
                print(made)
                flag = True
                break
            elif made2 == made2[::-1]:
                print(made2)
                flag = True
                break
            # 두 단어를 골라 펠린드롬을 만들수 있는지 확인해줍니다 
            # 펠린드롬이 만들어졌다면 만들어진 펠린드롬을 출력하고 만들어졌음을 표시해줍니다
        if flag:
            break
        # 펠린드롬이 만들어졌다면 반복을 멈추어줍니다
    else:
        print(0)
        # 펠린드롬이 만들어지지않아 break가 작동하지 않았다면 0을 출력해줍니다