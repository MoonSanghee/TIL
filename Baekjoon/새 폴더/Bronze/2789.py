word = input()

van_list = []
for i in 'CAMBRIDGE':
    van_list.append(i)

for i in word:
    if i not in van_list:
        print(i, end ='')