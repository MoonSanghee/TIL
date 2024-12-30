arr = []

for _ in range(7):
    name, people = input().split()
    people = int(people)
    arr.append((people, name))

arr.sort(key = lambda x : x[0], reverse = True)
print(arr[0][1])