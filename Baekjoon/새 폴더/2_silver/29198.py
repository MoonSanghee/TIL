n, m, k = map(int, input().split())
# 주어지는 문자열의 길이와 문자의 개수를 받고 사용할 단어의 수를 받아줍니다
arrs = []
for _ in range(n):
    arr = list(input())
    arr.sort()
    arrs.append(arr)
# n개의 단어를 받아 문자를 사전순으로 정렬한다음 리스트에 넣어줍니다
arrs.sort()
result = []
# 받은 단어를 사전순으로 정렬하고 k개의 단어를 넣을 리스트를 만들어줍니다
for i in range(k):
    result += arrs[i]
result.sort()
result = ''.join(result)
# k개의 단어를 더하고 문자들을 사전순으로 정렬하고 리스트에 든 문자를 공백이 없이 문자열로 더해줍니다
print(result)
# 결과를 출력해줍니다