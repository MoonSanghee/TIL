Man1 = input()
Man2 = input()

if (Man1 == "가위" and Man2 == "보") or (Man1 == "보" and Man2 == "바위") or (Man1 == "바위" and Man2 == "가위"):
    print("Result : Man1 Win!")
elif (Man2 == "가위" and Man1 == "보") or (Man2 == "보" and Man1 == "바위") or (Man2 == "바위" and Man1 == "가위"):
    print("Result : Man2 Win!")
else:
    print("Result : Draw")