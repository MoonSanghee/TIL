word = input()
# 주어지는 문장을 받아줍니다
k = ['K','O','R','E','A']
y = ['Y','O','N','S','E','I']

for i in word:
    if i == k[0]:
        k.remove(i)
        if len(k) == 0:
            print("KOREA")
            break
    if i == y[0]:
        y.remove(i)
        if len(y) == 0:
            print('YONSEI')
            break
    # 주어지는 문자열을 확인하며 찾는 두 단어중에 먼저 완성되는 단어를 출력하고 확인을 멈추어줍니다