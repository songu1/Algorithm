# LCS(Longest Common Subsequence, 최장 공통 부분 수열)
# 두 수열이 주어졌을 때, 모두의 부분수열이 되는 수열 중 가장 긴 것

# 입력 : 두 문자열(대문자로만 이루어짐, 최대 1000글자)
# 출력 : 두 문자열의 LCS 길이

# 알고리즘 힌트 조금 참고
# d를 2차원 배열로 생각하여 모든 경우의 LCS 구하기

import sys

str1 = list(map(str,sys.stdin.readline().rstrip()))
str2 = list(map(str,sys.stdin.readline().rstrip()))
n = len(str1)   # j
m = len(str2)   # i
d = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        # d[0][j] 또는 d[i][0] 일 때
        if i==0 or j==0:
            # 첫째 가로줄
            if i == 0 and j > 0:
                d[i][j] = d[i][j-1]
            # 첫째 세로줄
            elif i > 0 and j == 0:
                d[i][j] = d[i-1][j]
            # 두 수열의 문자가 일치할 때
            if str1[j] == str2[i]:
                d[i][j] = 1
        # i,j가 모두 0보다 클 때
        else:
            if str1[j] == str2[i]:
                d[i][j] = d[i-1][j-1] + 1
            else:
                d[i][j] = max(d[i-1][j], d[i][j-1])
        
print(d[m-1][n-1])

# ACAYKP
# CAPCAK      # 4 (ACAK)

# ABCDEF
# GBCDFE      # 4

# VREGDFELK
# VLSKD       # 3

# AAA
# AA          # 2

# CAPCK
# AA          # 1