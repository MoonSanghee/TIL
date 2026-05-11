tc = int(input())
# 테스트케이스가 몇개 주어지는지 받아줍니다
for t in range(tc):
    word = input()
    result = ''
    # 단어를 받고 결과를 담을 변수를 설정해줍니다 
    for i in word:
        if i not in 'aeiou':
            result += i
    # 모음이 아니라면 결과에 추가해줍니다
    print(f'#{t + 1} {result}')
    # 주어진 양식에 맞게 결과를 출력해줍니다