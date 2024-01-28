t = int(input())
# 주어질 테스트의 수를 받아줍니다.
for tc in range(t):
    n, m = map(int, input().split())
    # 두 리스트의 길이를 받아줍니다.
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    # 두 수열 리스트를 받아줍ㄴ디ㅏ.
    alist.sort()
    blist.sort()
    # 두 수열 리스트를 오름차순으로 정렬해줍니다.
    
    idx = 0
    # b리스트에서 마지막으로 확인한 인덱스 자리를 저장할 변수를 설정해줍니다.
    clist = []
    # c리스트를 만들어줍니다.
    for i in range(n):
        for j in range(idx, m - 1):
            if abs(blist[idx] - alist[i]) > abs(blist[idx + 1] - alist[i]):
                idx += 1
                # b리스트를 확인하며 절대값이 더 작다면 idx 값을 갱신해줍니다.
            else:
                clist.append(blist[idx])
                break
                # 갱신되지 않는다면 clist에 값을 넣고 break를 통해 a리스트의 다음 값을 확인해줍니다.
        else:
            clist.append(blist[idx])
            # b리스트의 마지막까지 break가 작동하지 않는다면 b리스트 마지막값을 c리스트에 넣도록 해줍니다.
    
    print(sum(clist))
    # c리스트 수열의 합을 구해서 출력해줍니다.