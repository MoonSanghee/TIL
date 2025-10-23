s = input()
# 주어지는 입력을 받아줍니다
if s == '(1)':
    print(0)
elif '(1' in s or '1)' in s or '()' in s:
    print(1)
else:
    print(2)
    # 필요한 이동을 출력해줍니다