n = int(input())
# 대출 신청 수를 받아줍니다
days = [0] * 32
# 31일 이하의 날짜가 주어지므로 사용하지 않을 0을 포함해 32개의 날짜에 대출 신청 건수를 담을 0을 넣어줍니다
for i in range(n):
    start, end = map(int, input().split())
    for j in range(start, end):
        days[j] += 1
# n개의 대출 요청을 받고 대출희망일의 대출도서수를 표시해줍니다
k = int(input())
# 책의 수를 받아줍니다
for i in days:
    if i > k:
        print(0)
        break
else:
    print(1)
# 도서보다 많은 대출 신청이 있는 날이 있다면 대출 불가를 아니면 가능을 출력해줍니다