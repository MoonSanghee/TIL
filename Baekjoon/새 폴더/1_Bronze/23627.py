word = input()
# 주어지는 문자열을 받아줍니다
if len(word) > 4 and word[-5:] == 'driip':
    print('cute')
else:
    print('not cute')
    # 귀엽다고 생각하는 문자열인지 확인한 결과를 출력해줍니다