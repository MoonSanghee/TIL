n, m = map(int, input().split())
# 주어지는 두 수를 받아줍니다
arr = [input() for _ in range(n)]
arr.sort()
# 주어지는 단어들을 받고 사전순으로 정렬해줍니다
print(arr[m - 1])
# 요청받은 순서의 단어를 출력해줍니다