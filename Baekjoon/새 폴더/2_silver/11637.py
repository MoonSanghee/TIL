t = int(input())
# 확인할 케이스가 몇개인지 받아줍니다.
for _ in range(t):
    n = int(input())
    # 후보자의 수를 받아줍니다.
    votes = [int(input()) for _ in range(n)]
    # 후보자들의 득표를 받아줍니다
    total = sum(votes)
    # 모든 득표의 합을 구해줍니다.
    max_votes = max(votes)
    max_count = votes.count(max_votes)
    won = votes.index(max_votes) + 1
    # 최다 득표와 최다 득표자를 확인하여줍니다.
    if max_count == 1:
        if total // 2 < max_votes:
            print(f"majority winner {won}")
        else:
            print(f"minority winner {won}")
    else:
        print("no winner")
    # 최다 득표자가 1명인지 과반 득표인지 확인하여 알맞은 형식으로 출력하여줍니다.