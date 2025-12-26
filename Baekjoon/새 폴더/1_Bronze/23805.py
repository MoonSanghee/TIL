base = ['@@@ @',
        '@ @ @',
        '@ @ @',
        '@ @ @',
        '@ @@@']
# 기본형태를 담아줍니다
n = int(input())
# 출력하고자하는 크기를 받아줍니다
for i in range(5):
    for _ in range(n):
        for j in range(5):
            for _ in range(n):
                print(base[i][j], end='')
        print()
# 주어진 형식에 맞게 모양을 출력해줍니다