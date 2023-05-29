# 그림 DFS - but BFS로 푸는게 이득임
# 큰 도화지에 있는 그림의 개수, 그림 중 넣이가 가장 넓은 것의 넓이를 출력하는 프로그램
# 그림 : 가로, 세로가 1로 연결된 것이 하나의 그림
# 그림의 넓이 : 그림에 포함된 1의 개수

# 입력 : 도화지의 세로크기 n(1~500)과 가로크기 m(1~500)
# 그림의 정보 (0:색칠 안된 부분, 1:색칠된 부분)
# 출력 : 그림의 개수
# 가장 넓은 그림의 넓이(그림이 하나도 없는 경우 0)

import sys
sys.setrecursionlimit(1000000)

# 입력
n,m=map(int,sys.stdin.readline().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

size=0  # 임의 추가

# dfs 함수
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
# def dfs(graph,x,y):
#     global size
#     # 방문처리
#     graph[x][y]=2
#     size += 1
#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if nx<0 or ny<0 or nx>=n or ny>=m:
#             continue
#         if graph[nx][ny]==1:
#             dfs(graph,nx,ny)
#     return
def dfs(graph,x,y):
    global size
    if x<0 or y<0 or x>=n or y>=m:
        return 
    if graph[x][y]==1:
        graph[x][y]=2
        size += 1
        dfs(graph,x-1,y)
        dfs(graph,x+1,y)
        dfs(graph,x,y-1)
        dfs(graph,x,y+1)
    return

# main 코드
count=0
maxsize=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            size=0
            dfs(graph,i,j)
            maxsize = max(maxsize, size)
            count += 1

print(count)
print(maxsize)


# 6 5
# 1 1 0 1 1
# 0 1 1 0 0
# 0 0 0 0 0
# 1 0 1 1 1
# 0 0 1 1 1
# 0 0 1 1 1
#
# 4
# 9