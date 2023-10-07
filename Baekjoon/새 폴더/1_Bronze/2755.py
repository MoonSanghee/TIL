n = int(input())
gradeSheet = {'A+': 4.3, 'A0': 4.0,' A-': 3.7,
'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
'F': 0.0}

totalCredit = 0
totalPoint = 0

for _ in range(n):
    subject, credits, grade = input().split()
    totalCredit += int(credits)
    totalPoint += int(credits) * gradeSheet[grade]

average = "%.2f" % (round(totalPoint/totalCredit + 10**-10, 2))
print(average)