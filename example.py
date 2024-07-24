# dfs, bfs (노드)
graph=[
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]

# dfs (노드)
def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

visited = [False] * 9
dfs(graph, 1, visited)

# bfs (노드)
from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * 9
bfs(graph, 1, visited)



# dfs, bfs 2차원
import sys
n,m=map(int,sys.stdin.readline().split())
graph=[]

# dfs
def dfs(map,x,y):
    if x<=-1 or x>n or y <=-1 or y>n:
        return False
    if map[x][y] == 0:
        map[x][y] = 1
        dfs(map,x-1,y)
        dfs(map,x+1,y)
        dfs(map,x,y-1)
        dfs(map,x,y+1)
        return True
    return False

for i in range(n):
    for j in range(m):
        dfs(graph,i,j)

# bfs
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(map,x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if map[nx][ny] == 0:
                continue
            if map[nx][ny] == 1:
                map[nx][ny] = map[x][y]+1
                queue.append((nx,ny))
    return map[n-1][m-1]

bfs(graph,0,0)