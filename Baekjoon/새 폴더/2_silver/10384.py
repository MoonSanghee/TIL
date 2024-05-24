t = int(input())
# 테스트 케이스의 수를 받아줍니다.
for tc in range(t):
    d = dict()
    for i in 'abcdefghijklmnopqrstuvwxyz':
        d[i] = 0
    # 딕셔너리에 모든 알파벳을 0개로 넣어줍니다.
    line = input()
    for i in line:
        if i.lower() in 'abcdefghijklmnopqrstuvwxyz':
            d[i.lower()] += 1
    # 문장의 문자가 알파벳이라면 딕셔너리에 값을 수정해줍니다.
    cnt = 3
    for i in d:
        cnt = min(cnt, d[i])
    # 딕셔너리를 순회하며 가장 적게나온 문자가 몇개인지 확인해줍니다.
    if cnt == 0:
        print(f"Case {tc + 1}: Not a pangram")
    elif cnt == 1:
        print(f"Case {tc + 1}: Pangram!")
    elif cnt == 2:
        print(f"Case {tc + 1}: Double pangram!!")
    else:
        print(f"Case {tc + 1}: Triple pangram!!!")
    # 주어진 양식에 맞게 출력해줍니다.