science = []
social = []

for _ in range(4):
    science.append(int(input()))
for _ in range(2):
    social.append(int(input()))

sciencepoint = sum(science) - min(science)
socialpoint = sum(social) - min(social)

print(sciencepoint + socialpoint)