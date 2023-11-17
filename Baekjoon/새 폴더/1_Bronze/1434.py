n, m = map(int, input().split())
# 상자와 책의 수를 받아줍니다.
boxes = list(map(int, input().split()))
books = list(map(int, input().split()))
# 책과 상자를 받아줍니다.
print(sum(boxes) - sum(books))
# 상자 용량의 합에 책 크기의 합을 뺀 값을 출력해줍니다.