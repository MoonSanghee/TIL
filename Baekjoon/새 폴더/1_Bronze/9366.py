for case in range(int(input())):
    li = sorted(map(int, input().split()))
    # 주어지는 세 변의 길이를 받아 오름차순으로 정렬해줍니다
    print(f"Case #{case+1}: ", end='')
    # 케이스 번호를 출력해줍니다
    if li[0]+li[1] <= li[2]:
        print("invalid!")
    elif li[0] == li[1] == li[2]:
        print("equilateral")
    elif li[0]==li[1] or li[1]==li[2] or li[2]==li[0]:
        print("isosceles")
    else:
        print("scalene")
    # 삼각형의 모양을 확인하여 결과를 출력해줍니다