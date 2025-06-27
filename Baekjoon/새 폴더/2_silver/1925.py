first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))
# 주어지는 세 좌표를 받아줍니다
points = sorted([first, second, third])
first, second, third = points
# 주어지는 좌표를 x값을 기준으로 오름차순 정렬해줍니다
a1, a2 = first
b1, b2 = second
c1, c2 = third

l1 = (a1 - b1) ** 2 + (a2 - b2) ** 2
l2 = (b1 - c1) ** 2 + (b2 - c2) ** 2
l3 = (c1 - a1) ** 2 + (c2 - a2) ** 2
# 세 좌표를 이용하여 세 변의 길이를 구하여줍니다
arr = [l1, l2, l3]
arr.sort()
# 세 변을 리스트에 넣고 오름차순으로 정렬해줍니다
if (b1 - a1) * (c2 - b2) == (b2 - a2) * (c1 - b1):
    print("X")
    # 외적을 이용하여 세 좌표가 한 선위에 존재한다면 삼각형이 아니라고 출력해줍니다
elif l1 == l2 == l3:
    print("JungTriangle")
elif l1 == l2 or l2 == l3 or l3 == l1:
    if arr[2] > arr[1] + arr[0]:
        print("Dunkak2Triangle")
    elif arr[2] == arr[0] + arr[1]:
        print("Jikkak2Triangle")
    else:
        print("Yeahkak2Triangle")
else:
    if arr[2] > arr[1] + arr[0]:
        print("DunkakTriangle")
    elif arr[2] == arr[0] + arr[1]:
        print("JikkakTriangle")
    else:
        print("YeahkakTriangle")
    # 삼각형이 성립한다면 삼각형의 형태를 확인해 어떠한 삼각형인지 출력해줍니다