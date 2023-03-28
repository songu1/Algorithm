# 정수 n이 주어졌을 때 n을 1,2,3으로 나타내는 방법의 수 - 초기값 설정 주의!!

# 입력 : 테스트 케이스 수 T
# 각 테스트케이스별 정수 n (1~11)
# 출력 : 각 테스트케이스마다 n을 1,2,3의 합으로 나타내는 방법의 수

# 점화식 : d[i] = d[i-1]+d[i-2]+d[i-3]

import sys

T=int(sys.stdin.readline())
result=[]

for t in range(T):
    n=int(sys.stdin.readline())
    d=[0]*12
    d[1]=1
    d[2]=2
    d[3]=4
    for i in range(4,n+1):
        d[i]=d[i-1]+d[i-2]+d[i-3]
    result.append(d[n])

print(*result,sep="\n")

# 3
# 4
# 7
# 10
# # 7
# # 44
# # 274
