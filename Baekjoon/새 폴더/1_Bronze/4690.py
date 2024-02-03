for a in range(2,101):
    for b in range(2,101):
        for c in range(b + 1,101):
            for d in range(c + 1,101):
                if a * a * a == (b * b * b + c * c * c + d * d * d):
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
                    # a의 오름차순으로 출력해줘야하므로 a부터 b, c, d를 차례로 반복해줍니다.
                if a * a * a < (b * b * b + c * c * c + d * d * d):
                    break
                # 세제곱 세 수의 합이 a의 세제곱보다 커졌으면 d값을 더 반복할 필요 없으므로 break를 걸어줍니다.