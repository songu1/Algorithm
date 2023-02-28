# n가지 종류의 화폐
# 이 화폐들의 개수를 최소한으로 이용하여 그 가치의 합이 m원이 되도록
# m원을 만들기위한 최소한의 화폐개수를 출력하는 프로그램

# 입력 : n,m (1 <= n <= 100, 1<=m <= 10000)
# n개의 줄에 각 화폐의 가치 (1~10000)
# 출력 : 최소화폐의 개수 (불가능시 -1 출력)

import sys

n,m=map(int,sys.stdin.readline().split())
coin=[]
for i in range(n):
    coin.append(int(sys.stdin.readline()))

d=[m+1]*(m+1)
d[0]=0

for i in range(1,m+1):
    for c in coin:
        if i-c>=0:
            d[i]=min(d[i],d[i-c]+1)

if d[m]==m+1:
    print(-1)
else:
    print(d[m])


# 2 15
# 2
# 3           # 5

# 3 4
# 3
# 5
# 7           # -1


# 이코테 풀이
# n,m=map(int,input().split())
# array=[]
# for i in range(n):
#     array.append(int(input()))

# # 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
# d[0]=0
# for i in range(n):
#     for j in range(array[i],m+1):
#         if d[j-array[i]] != 10001:  # i-k원을 만드는 방법이 존재하는 경우
#             d[j] = min(d[j],d[j-array[i]]+1)

# # 계산된 결과 출력
# if d[m]==10001:     # 최종적으로 m원을 만드는 방법이 없는 경우
#     print(-1)
# else:
#     print(d[m])