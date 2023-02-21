from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0, 0))
    # 시작값(0)과 계산해야할 자리값을 q에 넣어줍니다.
    while q:
        l, num = q.popleft()
        if l == len(numbers):
            if num == target:
                answer += 1
                # l이 numbers의 길이와 같아지면 값이 target과 같은지 확인하고
                # answer에 값을 갱신해줍니다.
        elif l < len(numbers):
            q.append((l + 1, num + numbers[l]))
            q.append((l + 1, num - numbers[l]))
            # l이 numbers의 길이보다 짧다면 더하고 빼는 값과 l + 1을 튜플로 q에
            # 넣어줍니다.
    return answer