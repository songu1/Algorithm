# ** 풀이 조금 참고 **
# 동빈 n개의 동전을 가짐
# n개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값

# 동전의 개수를 나타내는 양의 정소 n (1<=n<=1000)
# 각 동전의 화폐단위를 나타내는 n개의 자연수(공백 구분)

# 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값

# 알고리즘
# 동전 화폐 단위를 오름차순 정렬
# 1부터 차례대로 단계를 거쳐 특정한 금액(target)을 만들 수 있는지 확인
# 1부터 target-1까지 모든 금액을 만들 수 있다고 가정
    # 화폐의 단위가 작은 순서대로 동전 확인
    # 현재 확인하는 동전을 이용해 target금액을 만들 수 있는지 확인
    # 현재 확인하는 동전금액이 target 이하여야 그 동전을 이용하여 target 만들 수 있음
    # 해당 target 금액을 만들 수 있으면 target값을 업데이트

import sys
n=int(sys.stdin.readline())
coin=list(map(int,sys.stdin.readline().split()))
coin.sort()

target=1

for i in coin:
    if i > target:
        break
    else:
        target+=i

print(target)



# 5
# 3 2 1 1 9         # 8

# 3
# 3 5 7             # 1

# 4
# 1 3 2 4           # 11