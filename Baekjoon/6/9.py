# 6-9 문제번호 2941

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# 크로아티아 문자를 표현해주는 문자열들을 리스트로 생성
word = input()
# 인풋값 설정
for i in croatia:
    word = word.replace(i, '*')
    # 리스트 안에 있는 문자열들을 replace를 이용하여 
    # 다른 특정한 값으로 변경
print(len(word))
#변경후 문자열의 길이 출력