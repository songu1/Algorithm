# 친구
# 가장 유명한 사람 구하는 방법
    # 각 사람의 "2-친구" 구하기
        # A와 B가 친구 : a-b 또는 a-b-c
    # 가장 유명한 사람 : 2-친구 수가 가장 많은 사람
# 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램

# 입력 : 사람 수 n (1~50)
# n개의 줄에 각 사람이 친구이면 Y 아니면 N
# 가장 유명한 사람의 2-친구의 수를 출력

# 거리가 1,2인 값들의 수가 가장 많은 사람의 친구수 출력
# 2차원 배열로 친구 사이의 거리 계산 -> 가장 많은 1,2 거리의 친구를 가진 사람의 친구 수 출력

import sys

INF = 50
n = int(sys.stdin.readline())
graph = [[0]*n for _ in range(n)]
for i in range(n):
    input = list(map(str,sys.stdin.readline().rstrip()))
    for j in range(n):
        if input[j] == 'Y':
            graph[i][j] = 1
        elif i == j:
            graph[i][j] = 0
        else:
            graph[i][j] = INF

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# 가장 유명한 사람 친구 수 확인하기
maxCount = -1
for i in range(n):
    count = 0
    for j in range(n):
        if graph[i][j] in (1,2):
            count += 1
    maxCount = max(count, maxCount)
print(maxCount)



# 3
# NYY
# YNY 
# YYN                 # 2

# 3
# NNN
# NNN
# NNN                 # 0

# 5
# NYNNN
# YNYNN
# NYNYN
# NNYNY
# NNNYN               # 4

# 10
# NNNNYNNNNN
# NNNNYNYYNN
# NNNYYYNNNN
# NNYNNNNNNN
# YYYNNNNNNY
# NNYNNNNNYN
# NYNNNNNYNN
# NYNNNNYNNN
# NNNNNYNNNN
# NNNNYNNNNN          # 8

# 15
# NNNNNNNNNNNNNNY
# NNNNNNNNNNNNNNN
# NNNNNNNYNNNNNNN
# NNNNNNNYNNNNNNY
# NNNNNNNNNNNNNNY
# NNNNNNNNYNNNNNN
# NNNNNNNNNNNNNNN
# NNYYNNNNNNNNNNN
# NNNNNYNNNNNYNNN
# NNNNNNNNNNNNNNY
# NNNNNNNNNNNNNNN
# NNNNNNNNYNNNNNN
# NNNNNNNNNNNNNNN
# NNNNNNNNNNNNNNN
# YNNYYNNNNYNNNNN     # 6