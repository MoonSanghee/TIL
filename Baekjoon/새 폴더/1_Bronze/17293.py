n = int(input())
left = n
# 병의 수와 남은 병의 수를 담을 변수를 설정해줍니다
while left > 0:
    if left == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    elif left == 2:
        print(f"{left} bottles of beer on the wall, {left} bottles of beer.")
        print("Take one down and pass it around, 1 bottle of beer on the wall.")
    else:
        print(f"{left} bottles of beer on the wall, {left} bottles of beer.")
        print(f"Take one down and pass it around, {left - 1} bottles of beer on the wall.")
    print()
    left -= 1
# 남은 병의 수를 확인하여 주어진 형식에 맞춰 출력해줍니다
print("No more bottles of beer on the wall, no more bottles of beer.")
print(f"Go to the store and buy some more, {n} bottle{'s' if n != 1 else ''} of beer on the wall.")
# 남은 병이 없으면 반복을 완료하고 주어진 형식을 출력해줍니다