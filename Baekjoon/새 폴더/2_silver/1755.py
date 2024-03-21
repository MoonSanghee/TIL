d = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', 
     '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
# 아라비아 숫자와 영어를 키 밸류로 묶어 d라는 딕셔너리에 넣어줍니다.
m, n = map(int, input().split())
li = []
# 주어지는 범위 두 수를 받고 수를 넣어줄 리스트를 만들어줍니다.
for i in range(m, n + 1):
    word = ''
    for c in str(i):
        word += d[c]
    li.append([i, word])
    # 수의 각 자리를 확인하여 문자열 형태로 모아 수, 영어를 리스트 형태로 묶어 li 리스트에 넣어줍니다. 
li.sort(key=lambda x:x[1])
# 리스트를 사전순으로 오름차순 정렬해줍니다.
for i in range(len(li)):
    if i%10 == 0 and i!= 0:
        print()
    print(li[i][0], end=' ')
    # 10개씩 끝어 각 수 마다 띄우고 출력해줍니다.