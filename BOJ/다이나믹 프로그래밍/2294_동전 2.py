# 동전 2
# n가지 종류의 동전 -> 가치의 합이 k원이면서 동전의 개수가 최소가 되도록
    # 각각의 동전은 몇개라도 사용 가능

# 입력 : n(1~100), k(1~10000)
# n개의 줄에 동전의 가치(1~100,000) - 가치가 같은 동전이 여러번 주어질 수도 있음
# 출력 : 사용한 동전의 최소개수, 불가능이면 -1

# 최대 동전 100개, 가치의 최대합 10000, 동전의 가치 최대 100,000
    # -> 동전 가치가 10001 ~ 100,000인 것은 사용 불가능

import sys

# 입력
n,k=map(int,sys.stdin.readline().split())
value=[]
for i in range(n):
    value.append(int(sys.stdin.readline()))

# main
d=[k+1]*(k+1)     # 최소 횟수
d[0]=0

for i in range(1,k+1):
    for v in value:
        if i >= v:
            d[i]=min(d[i],d[i-v]+1)

if d[k]==k+1:
    print(-1)
else:
    print(d[k])


# 3 15
# 1
# 5
# 12      # 3