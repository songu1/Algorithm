# 욕심쟁이 판다
# n*n 크기의 대나무 숲에서 판다가 대나무 먹고 상하좌우 이동
# 옮긴 지역은 그 전 지역보다 대나무가 많아야함
    # 어떤 지점에서 출발, 어떤 곳으로 이동해야하는지
# n*n 크기의 대나무 숲 -> 판다가 최대한 많은 칸을 이동하려면 어떤 경로를 통해 이동해야하는지

# 입력 : 대나무 숲의 크기 n(1~500)
# 대나무 숲의 정보 (각 지역의 대나무 양 : 정수값, 1~1000000)
# 출력 : 판다가 이동할 수 있는 칸의 수의 최댓값

# DP + DFS

import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline())
forest=[]
for _ in range(n):
    forest.append(list(map(int,sys.stdin.readline().split())))
dp = [[0]*n for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(forest,x,y,dp):
    # 방문처리
    dp[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if forest[nx][ny] > forest[x][y]:
            if dp[nx][ny] == 0:
                dfs(forest,nx,ny,dp)
            dp[x][y] = max(dp[x][y], dp[nx][ny]+1)
    return

maxValue = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            dfs(forest,i,j,dp)
        maxValue = max(maxValue,dp[i][j])
print(maxValue)

# 4
# 14 9 12 10
# 1 11 5 4
# 7 15 2 13
# 6 3 16 8        # 4