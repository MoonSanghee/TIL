li = ["baby", "sukhwan", "tururu", "turu", "very", "cute", "tururu", 
      "turu", "in", "bed", "tururu", "turu", "baby", "sukhwan"]
# 가사를 받아줍니다
n = int(input()) - 1
# 몇 번째 단어를 찾는지 받고 0번 인덱스를 사용하므로 1을 빼줍니다
k = n // 14
# 14로 나눈 몫을 구해줍니다
if n % 14 in [3, 7, 11]:
    print(f"tu+ru*{k + 1}" if k >= 4 else "turu" + "ru" * k)    
elif n % 14 in [2, 6, 10]:
    print(f"tu+ru*{k + 2}" if k >= 3 else "tururu" + "ru" * k)    
else:
    print(li[n % 14])
# 출력될 가사의 파트를 찾아 결과를 출력해줍니다