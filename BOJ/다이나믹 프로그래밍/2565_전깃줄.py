# 전깃줄
# 전봇대 a,b 사이에 전깃줄 추가
# 전깃줄이 교차하는 경우 많음 -> 몇개의 전깃줄을 없애 전깃줄이 교차하지 않도록
# 전깃줄이 전봇대에 연결되는 위치는 위부터 차례대로 번호
# 전깃줄 개수, 전깃줄들이 두 전봇대에 연결된 위치 번호 -> 남아있는 전깃줄이 서로 교차하지 않기 위해 없애야하는 전깃줄의 최소개수

# 입력 : 전깃줄의 개수(1~100)
# 전깃줄이 a전봇대와 연결되는 위치번호, b전봇대와 연결되는 위치번호 ( 1~500)
    # 같은 위치에는 하나의 전깃줄만 연결됨
# 출력 : 남아있는 모든 전깃줄이 서로 교차하지 않게 하기위해 없애야하는 전깃줄의 최소개수

# LIS 알고리즘 : 가장 긴 증가하는 부분수열
# 1차시도 실패 : 가장 긴 증가하는/감소하는 부분수열 중 최대값을 구하여 n-최대값을 수행
    # => 감소하는 수열은 전깃줄이 교차하는 것임

import sys

n = int(sys.stdin.readline())
string = []
for _ in range(n):
    string.append(list(map(int,sys.stdin.readline().split())))
string.sort()   # a전봇대의 전깃줄로 sort함

dp = [1]*n
maxDp = 0
for i in range(1,n):
    for j in range(i):
        # 가장 긴 증가하는 부분수열
        if string[i][1] > string[j][1]:
            dp[i] = max(dp[i],dp[j]+1)
        
    maxDp = max(maxDp, dp[i])

# print(dp)
print(n-maxDp)

# string = [0]*501
# maxA = 0
# for _ in range(n):
#     a,b = map(int,sys.stdin.readline().split())
#     string[a] = b
#     maxA = max(maxA,a)

# dp1 = [1]*(maxA+1)
# dp2 = [1]*(maxA+1)
# dp1[0] = 0
# dp2[0] = 0

# maxDp = 0

# for i in range(1,maxA):
#     if string[i] == 0:
#         continue
#     for j in range(1,i):
#         # 가장 긴 증가하는 부분수열
#         if string[i] > string[j]:
#             dp1[i] = max(dp1[i],dp1[j]+1)
        
#         # 가장 긴 감소하는 부분수열
#         if string[i] < string[j]:
#             dp2[i] = max(dp2[i], dp2[j]+1)
#     maxDp = max(maxDp, dp1[i])
#     maxDp = max(maxDp, dp2[i])

# print(dp1)
# print(dp2)
# print(n-maxDp)



# 8
# 1 8
# 3 9
# 2 2
# 4 1
# 6 4
# 10 10
# 9 7
# 7 6         # 3

# 5
# 1 3
# 3 1
# 2 5
# 4 6
# 6 4         # 2

# 2
# 1 2
# 4 1         # 1