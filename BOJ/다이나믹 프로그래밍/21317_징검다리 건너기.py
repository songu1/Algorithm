# 징검다리 건너기 - 벽부수고 이동하기와 살짝 비슷
# n개의 돌이 일렬로 나열, 돌 틈 사이에 산삼이 존재
# 마지막 돌 틈 사이에 있는 산삼을 캐기 -> 돌과 돌 사이를 점프하며 이동
    # +1 : 작은 점프                        - 소비 되는 에너지 돌 번호마다 다름
    # +2 : 큰 점프 (돌 1개 뛰어넘음)         - 소비 되는 에너지 돌 번호마다 다름 
    # +3 : 매우 큰 점프(돌 2개 뛰어넘음)     - 돌 번호와 상관없이 k만큼 에너지 소비 : 딱 1번만 가능
# 에너지를 최대한 아끼는 영재가 산삼을 얻기 위해 필요한 에너지의 최솟값

# 입력 : 돌의 개수 n(1~20)
# 1~n-1돌 까지 작은 점프를 하기 위해 필요한 에너지, 큰 점프를 하기 위해 필요한 에너지 (5000이하)
# k(5000이하)

# 출력 : 산삼을 얻기 위해 필요한 영재의 최소 에너지

# 알고리즘
# d: 필요한 에너지
# 1차 -> 틀림

import sys

n=int(sys.stdin.readline())
energy=[[]]
for i in range(1,n):
    energy.append(list(map(int,sys.stdin.readline().split())))
k=int(sys.stdin.readline())

d=[[100001,100001] for _ in range(n+1)]   # d[i][0] : 매우 큰 점프X / d[i][1] : 매우 

d[1][0]=0
if n>=2:
    d[2][0]=energy[1][0]
if n>=3:
    d[3][0]=min(d[2][0]+energy[2][0],energy[1][1])
if n>=4:
    for i in range(4,n+1):
        # 매우 큰 점프를 하지 않는 경우
        d[i][0]=min(d[i-1][0]+energy[i-1][0], d[i-2][0]+energy[i-2][1])
        # 매우 큰 점프를 하는 경우
        d[i][1]=d[i-3][0]+k
        d[i][1]=min(d[i][1], d[i-1][1]+energy[i-1][0])
        d[i][1]=min(d[i][1], d[i-2][1]+energy[i-2][1])
        # 매우 큰 점프O < 매우 큰 점프X  때만 d[i][1]에 기입
        if d[i][1]>=d[i][0]:
            d[i][1]=100001

print(min(d[n]))

# 5
# 1 2
# 2 3
# 4 5
# 6 7
# 4           # 5

# 9
# 1 2
# 2 3
# 4 5
# 6 7
# 8 9
# 8 9
# 10 11
# 1 2
# 4           # 10

# 20
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 4                   # 

# 20
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000 5000
# 5000