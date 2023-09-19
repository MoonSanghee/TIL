n = int(input())
# 단어가 몇 쌍인지 받아줍니다.
for _ in range(n):
    worda, wordb = map(str, input().split())
    # 두 단어를 받아줍니다.
    lista = sorted(list(worda))
    listb = sorted(list(wordb))
    # 두 단어를 리스트로 만들어 정렬시켜줍니다.
    if lista == listb:
        print('Possible')
    else:
        print('Impossible')
    # 두 리스트가 같은지 확인하고 맞는 값을 출력해줍니다.