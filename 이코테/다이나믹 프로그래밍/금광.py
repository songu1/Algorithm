# n*m 크기의 금광, 각 칸은 특정한 크기의 금이 들어있음
# 채굴자는 첫번째 열부터 금을 캠 (첫번째 열의 어느 행에서든 출발 가능)
# m-1번에 걸쳐서 (오른쪽 위, 오른쪽, 오른쪽 아래) 중 하나의 위치로 이동해야함
# 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램

# 입력 : 테스트케이스 T (1~1000)
# 매 테스트 케이스
    # n,m (1~20)
    # n*m개의 위치에 매장된 금의 개수 (1~100)
# 출력 : 테스트케이스마다 채굴자가 얻을 수 있는 금의 최대 크기

#  1   3   3   2
# '2'  1   4   1
#  0  '6' '4' '7'       얻을 수 있는 금의 최대 크기 :19

import sys

t=int(sys.stdin.readline())
result=[]
for tc in range(t):
    inarr=[]
    arr=[]
    # 입력
    n,m=map(int,sys.stdin.readline().split())
    inarr=list(map(int,sys.stdin.readline().split()))
    d=[[0]*m for _ in range(n)]
    for i in range(n):
        arr.append(inarr[m*i:m*i+m])       # arr[i][ ] 설정
        d[i][0]=arr[i][0]
    # 다이나믹 프로그래밍
    for j in range(1,m):
        for  i in range(n):
            if i==0 and i==(n-1):
                d[i][j]=max(d[i][j-1])+arr[i][j]
            elif i==0:
                d[i][j]=max(d[i][j-1],d[i+1][j-1])+arr[i][j]
            elif i==(n-1):
                d[i][j]=max(d[i-1][j-1],d[i][j-1])+arr[i][j]
            else:
                d[i][j]=max(d[i-1][j-1],d[i][j-1],d[i+1][j-1])+arr[i][j]      
    # 최댓값 선택
    amax=-1
    for i in range(n):
        if d[i][m-1]>=amax:
            amax=d[i][m-1]
    result.append(amax)

print(*result,sep="\n")


# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
# # 19
# # 16

# 이코테 풀이
# for tc in range(int(input())):
#     n,m=map(int,input().split())
#     array=list(map(int,input().split()))
#     # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
#     dp=[]
#     index=0
#     for i in range(n):
#         dp.append(array[index:index+m])
#         index+=m
#     # 다이나믹 프로그래밍 진행
#     for j in range(1,m):
#         # 왼쪽 위에서 오는 경우
#         if i==0: left_up =0
#         else: left_up=dp[i-1][j-1]
#         # 왼쪽 아래에서 오는 경우
#         if i == n-1: left_down=0    
#         else: left_down=dp[i+1][j-1]
#         # 왼쪽에서 오는 경우
#         left=dp[i][j-1]
#         dp[i][j]=dp[i][j] + max(left_up, left_down, left)
#     result=0
#     for i in range(n):
#         result = max(result, dp[i][m-1])