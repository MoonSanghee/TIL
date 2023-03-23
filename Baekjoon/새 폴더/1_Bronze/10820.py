import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    # 각 줄의 입력을 line으로 받아줍니다.
    if not line:
        break
    # line 값이 없다면 반복을 멈추어줍니다.
    cnt = [0, 0, 0, 0]
    # 소문자, 대문자, 숫자, 공백을 저장해줄 0이 4개 들어간 리스트를 만들어줍니다.
    for i in line:
        # 라인을 순회하며
        if i.islower():
            cnt[0] += 1
        elif i.isupper():
            cnt[1] += 1
        elif i.isdigit():
            cnt[2] += 1
        elif i.isspace():
            cnt[3] += 1
        # 각 자리를 확인하여 맞는 값을 형태를 1 추가해줍니다.
    print(*cnt)
    # 리스트 안에 인덱스 값들을 출력해줍니다.

    
# while True :
#     try :
#         text_lst = list(input())
#         cnt = [0, 0, 0, 0]
#         for i in range(len(text_lst)) :
#             if text_lst[i] == " " :
#                 cnt[3] += 1
#             elif 65 <= ord(text_lst[i]) <= 90 :
#                 cnt[1] += 1
#             elif 97 <= ord(text_lst[i]) <= 122 :
#                 cnt[2] += 1
#             else :
#                 cnt[0] += 1
#             ord함수를 이용하여 각 자리값을 확인하여 형태를 확인해주고 세어줍니다.
#         print(*cnt)
#     except EOFError :
#         break
#       EOFError인 상황은 입력이 없는 상태이므로 반복을 멈추어줍니다.