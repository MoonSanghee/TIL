tc = int(input())
# 테스트 케이스의 갯수를 받아줍니다.
for _ in range(tc):
    blank = input()
    # 테스트 케이스 사이에 공백이 입력받아줍니다.
    n, m = map(int, input().split())
    # n, m을 받아줍니다.
    sejoon = list(map(int, input().split()))
    sebi = list(map(int, input().split()))
    # 세준이와 세비의 병력상태를 받아줍니다.
    if max(sejoon) >= max(sebi):
        print('S')
    else:
        print('B')
    # 병사가 한 명 남을때까지 전투가 계속되고 양쪽에 가장 약한 병사가 같으면
    # 세비의 병사가 임의로 죽으므로 가장 강한 병사가 세비에게 있으면 B를 아니면 S를 출력해줍니다.