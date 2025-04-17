import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# 메모장에 기록할 키워드의 개수와 쓸 글의 수를 받아줍ㄴ디ㅏ
memo = set()
for _ in range(n):
    memo.add(input().strip())
# 메모장에 작성하는 키워드를 셋을 만들어 담아줍니다
for _ in range(m):
    keywords = set(input().strip().split(','))
    memo -= keywords
    print(len(memo))
    # 글별로 사용하는 키워드를 받고 메모장에 있는 키워드를 빼고 남은 메모장의 키워드 개수를 출력해줍니다