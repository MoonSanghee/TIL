n = int(input())
# 단어의 개수를 받아줍니다.
for _ in range(n):
    word = input()
    # 단어를 받아줍니다.
    new = word[0].upper() + word[1:]
    # 첫 글자를 upper 메서드를 이용하여 대문자로 변환하여주고 문자열의 1번 인덱스 이후의 값들을 더해줍니다.
    print(new)
    # 새로 만든 문자를 출력해줍니다.
