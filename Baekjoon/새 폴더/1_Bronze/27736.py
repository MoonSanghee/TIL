n = int(input())
votes = list(map(int, input().split()))
# 투표인원과 투표 결과를 받아줍니다.
if votes.count(0) >= len(votes) / 2:
    print('INVALID')
# 기권이 절반 이상이면 무효처리를하고
else:
    if sum(votes) > 0:
        print('APPROVED')
    else:
        print('REJECTED')
    # 절반이 안 되면 투표 결과를 출력해줍니다.