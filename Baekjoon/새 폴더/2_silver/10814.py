n = int(input())
members = []
for i in range(n):
    member = list(map(str, input().split()))
    member[0] = int(member[0])
    members.append(member)

members = sorted(members, key = lambda x : x[0])
for i in members:
    print(*i)