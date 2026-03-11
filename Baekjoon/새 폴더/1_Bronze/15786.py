N, M = map(int, input().split())
S = input()
# 원본 알파벳의 수와 포스트잇의 수를 받고 문자열 S를 받아줍니다
for _ in range(M):
    word = input()
    # 포스트잇의 단어를 받아줍니다
    idx = 0
    for i in word:
        if i == S[idx]:
            idx += 1
            if idx == N:
                print('true')
                break
    else:
        print('false')
        # 포스트잇의 단어를 순회하며 원본 알파벳이 모두 나오는지 확인하여 결과를 출력해줍니다