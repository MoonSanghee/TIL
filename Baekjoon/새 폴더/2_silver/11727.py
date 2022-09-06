n = int(input())
cnt = [1, 3]
for i in range(2, 1001):
    cnt.append(cnt[i - 1] + 2 * (cnt[i - 2]))
print(cnt[n - 1]%10007)