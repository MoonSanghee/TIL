N = int(input())
list_input_1 = list(map(int, input().split()))
list_1 = list(set(list_input_1))
dic_1 = {}

for i in range(len(list_1)):
    dic_1[list_1[i]] = 0

for i in list_input_1:
    dic_1[i] += 1


M = int(input())
list_input_2 = list(map(int, input().split()))

for i in list_input_2:
    print(dic_1.get(i, 0), end = ' ')

# print(dic_1)