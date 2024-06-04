fatherbody, fathertail = input().split()
motherbody, mothertail = input().split()
# 부모의 몸통과 꼬리 색을 받아줍니다.
arr = [fatherbody, fathertail, motherbody, mothertail]
arr.sort()
# 부모에게 받을수 있는 색을 리스트에 담고 정렬을 실행해줍니다.
coms = []
for i in range(4):
    for j in range(4):
        if (arr[i], arr[j]) not in coms:
            coms.append((arr[i], arr[j]))
# 색을 순회하며 만든적 없는 조합이 나오면 조합 리스트에 추가해줍니다.
for com in coms:
    print(*com)
    # 만들수있는 조합을 차례대로 출력해줍니다.