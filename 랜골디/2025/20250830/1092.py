import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)
m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)
# 크레인과 박스의 정보를 받아 내림차순으로 정렬해줍니다
result = 0
if boxes[0] > cranes[0]:
    print(-1)
    # 가장 무거운 짐을 옮길수 없다면 -1을 출력해줍니다
else:
    while boxes:
        passed = 0
        for i in range(n):
            for j in range(passed, len(boxes)):
                if boxes[j] <= cranes[i]:
                    boxes.pop(j)
                    passed = j
                    break
        result += 1
        # 각 시간마다 옮길 수 있는 박스를 제거해줍니다
    print(result)
    # 걸린 시간을 출력해줍니다