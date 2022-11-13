n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
stack = []

def check():
    if len(stack) < m:
        for i in li:
            stack.append(i)
            check()
            stack.pop()
    else:
        print(*stack)
check()
# 주어진 리스트를 정렬하고 재귀를 통해 차례대로 넣어주는 함수를 구현하였습니다.
# 그리고 넣은 값의 개수가 원하는 값만큼 들어갔을때 리스트안의 값들을 출력해 주었습니다.