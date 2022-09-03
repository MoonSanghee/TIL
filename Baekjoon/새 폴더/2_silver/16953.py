start, a = list(map(int, input().split()))

cnt = 1
while start != a:
    cnt += 1
    check = a
    if a % 10 == 1:
        a //= 10
    elif a % 2 == 0:
        a //= 2
    
    if check == a:
        print(-1)
        break
else:
    print(cnt)



# bfs 이용한 풀이
# from collections import deque
# a,b = map(int,input().split())
# q = deque()
# q.append((a,1))
# r = 0

# while(q):
#     n,t = q.popleft()
#     if n > b:
#         continue
#     if n == b:
#         print(t)
#         break
#     q.append((int(str(n)+"1"),t+1))
#     q.append((n*2,t+1))
# else:
#     print(-1)