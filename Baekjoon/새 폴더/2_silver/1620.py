import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dict = {}

for i in range(1, n + 1):
    info = input().strip()
    dict[info] = i
    dict[i] = info
    # 입력되는 포켓몬 이름과 번호를 맞춰주기위해 1부터 n개의 이름을 입력받아
    # 딕셔너리에 이름 : 번호, 번호 : 이름 을 키 : 밸류 값으로 딕셔너리에 넣어줍니다.

for i in range(m):
    word = input().strip()
    # for i in range(10):
    #     if str(i) in word:
    #         print(dict[int(word)])
    #         break
    # else:
    #     print(dict[word])
    if word.isdigit():
        # m번만큼 입력되는 값이 숫자인지 확인하여 딕셔너리에 저장된 밸류값들 출력해줍니다.
        print(dict[int(word)])
    else:
        print(dict[word])

# 숫자만으로 이루어졌는지 확인하는 isdigit이라는 메서드를 알게되었습니다.