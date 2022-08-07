import sys

sys.stdin = open("1216_input.txt", "r")

test_case = 10
for test in range(1, test_case + 1):
    num = int(input())
    
    seet = []
    cnt = 1
    for _ in range(100):
        line = list(input())
        seet.append(line)
    # 100*100 크기의 2중 리스트 형태로 저장해 준다.
    for i in range(100):
        for j in range(100):
            word = []
            for k in range(100):
                if j + k < 100 :
                    word += seet[i][k + j]
                if word == word[::-1]:
                    if cnt < len(word):
                        cnt = len(word)
                        # 각 행을 돌면서 열의 특정 위치에서 끝까지 값을 추가하며 추가한 자리까지의 값을 뒤집은 값과 같을 경우 길이를 그 떄의 길이를 최대 단어 길이와 비교하여 갱신해준다.
            if len(word) == cnt:
                break
            

    for i in range(100):
        for j in range(100):
            word = []
            for k in range(100):
                if j + k < 100 :
                    word += seet[j + k][i]

                if word == word[::-1]:
                    if cnt < len(word):
                        cnt = len(word)
            if len(word) == cnt:
                break

    print(f'#{test} {cnt}')
