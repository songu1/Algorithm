# 빙산
# 2차원 배열에 빙산 표시
# 빙산의 각 부분별 높이 정보 : 각 칸에 양의 정수로 저장
# 바다 : 0
# 1년마다 해당 칸의 동서남북 방향 0칸 개수만큼 줄어듦
# 한 덩어리의 빙산 -> 빙산이 두덩어리 이상으로 분리되는 최초의 시간

# 입력 : 2차원 배열의 행 n, 열 m의 개수 (3~300)
# 배열을 나타내는 정수 (0~10)
# 출력 : 빙산이 분리되는 최초의 시간 (빙산이 다 녹을 때까지 분리되지 않으면 0 출력)

# 1차 시도 : 59%에서 시간초과

import sys
sys.setrecursionlimit(1000000)

n,m = map(int, sys.stdin.readline().split())
graph=[]
frozen=[]
visited=[[False]*m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if graph[i][j] != 0:
            frozen.append((i,j))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
# melt 함수
def melt(graph,frozen):
    count=[0]*len(frozen)
    # 상하좌우 탐색
    for i in range(len(frozen)):
        x,y = frozen[i]
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                count[i] += 1
    # graph값, frozen값 구하기
    for i in range(len(frozen)-1,-1,-1):    # frozen 반대부터
        x,y = frozen[i]
        graph[x][y] -= count[i]
        if graph[x][y] <= 0:
            graph[x][y] = 0
            del frozen[i]
    return graph
                    
# dfs 함수 - 덩어리수 찾는 함수
def dfs(graph,x,y,visited):
    # 방문처리
    visited[x][y]=True
    # 주위 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if graph[nx][ny]>0 and visited[nx][ny]==False:
            dfs(graph,nx,ny,visited)
    return True

# main 코드
count=0
time=0
while count<2:
    time += 1
    melt(graph,frozen)
    if len(frozen) == 0:
        time = 0
        break     
    count=0
    for i in range(len(frozen)):
        x,y = frozen[i]
        if visited[x][y]==False:
            if dfs(graph,x,y,visited):
                count += 1
    visited=[[False]*m for _ in range(n)]
  
print(time)

# 5 7
# 0 0 0 0 0 0 0
# 0 2 4 5 3 0 0
# 0 3 0 2 5 2 0
# 0 7 6 2 4 0 0
# 0 0 0 0 0 0 0       # 2