T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    N, M = map(int, input().split())
    words =[input() for _ in range(N)]
    # 주어지는 단어의 길이와 단어의 개수를 받고 단어들을 리스트에 담아줍니다
    solo = 0
    team = []
    result = 0
    # 혼자 팰린드롬을 이루는 단어의 최장 길이를 담을 변수와 재배열하여 팰린드롬을 만들수있는 단어들, 결과를 담을 변수를 설정해줍니다
    for word in words:
        if word == word[::-1]:
            solo = max(solo, len(word))
        elif word[::-1] in words:
            team.append(word)
    # 주어진 단어중에 뒤집힌 단어가 목록중에 존재한다면 재배열하여 팰린드롬을 이룰수있으므로 리스트에 넣고
    # 원래 팰린드롬은 가장 긴 하나만 사용할수있으므로 가장 긴것을 확인해줍니다
    for i in team:
        result += len(i)
    # 재배열할때 사용하는 단어들의 길이를 더해줍니다
    print(f'#{t + 1} {result + solo}')
    # 결과를 주어진 양식에 맞게 출력해줍니다