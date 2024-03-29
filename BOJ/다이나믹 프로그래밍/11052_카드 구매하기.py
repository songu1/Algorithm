# 카드 구매하기
# ps카드 : 각 카드에 등급을 나타내는 색이 칠해짐
    # 전설카드, 레드, 오렌지, 퍼플, 블루, 청록, 그레이
# 카드팩으로 구매가능 : 1개, 2개, .. n개의 카드가 포함된 파드팩
# 돈을 최대한 많이 지불해서 카드 n개 구매, 카드팩 중복 가능
    # 예시 : P1=1, P2=5, P3=6, P4=7 -> 4개의 카드 - 최대 10원
# 카드팩 가격 -> n개의 카드를 구매하기 위해 민규가 지불해야하는 금액의 최댓값
# 구매한 카드팩에 포함되어 있는 카드 개수의 합은 n이어야함

# 입력 : 민규가 구매하려는 카드의 개수 n(1~1000)
# 카드팩의 가격(1~10000)
# 출력 : 카드 n개를 갖기위해 지불해야하는 금액의 최댓값

import sys

n = int(sys.stdin.readline())
p = [0]
d = [0]
p += list(map(int,sys.stdin.readline().split()))
d = p[:]

for i in range(1,n+1):
    for j in range(1,i//2+1):
        d[i] = max(d[i], d[j]+d[i-j])

print(d[n])



# 4
# 1 5 6 7         # 10

# 5
# 10 9 8 7 6      # 50

# 10
# 1 1 2 3 5 8 13 21 34 55     # 55

# 10
# 5 10 11 12 13 30 35 40 45 47        # 50

# 4
# 5 2 8 10        # 20

# 4
# 3 5 15 16       # 18