n = input()
arr = [0] * (len(n) + 1)
# 주어지는 수와 누적합을 담을 n보다 1만큼 더 긴 리스트을 만들어줍니다
for i in range(len(n)):
    arr[i + 1] = arr[i] + int(n[i])
# 누적합을 구해 넣어줍니다
for length in range(len(n), 1, -1):
    if length % 2 != 0:
        continue
    # 길이가 홀수이면 반으로 나누어지지 않으므로 짝수만 확인을 해줍니다
    for i in range(len(n) - length + 1):
        mid = i + length // 2
        end = i + length
        # 찾고자하는 수의 중간위치와 마지막 위치를 확인해줍니다
        left = arr[mid] - arr[i]
        right = arr[end] - arr[mid]
        if left == right:
            print(length)
            exit()
            # 크리 문자열이 성립하면 길이를 출력하고 작동을 멈추어줍니다
            # 이중 반복을 한 번에 멈추기 위해 break가 아닌 exit을 이용하여 멈추어줍니다