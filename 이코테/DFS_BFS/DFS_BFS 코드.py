# DFS

# DFS 구현 - 재귀함수(스택)
def dfs(graph,v,visited):
    # 현재 노드 방문처리
    visited[v]=True
    print(v, end=' ')
    # 현재노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

# DFS 구현 - 2차원 배열로 주어질 때
import sys
n,m=map(int,sys.stdin.readline().split())
graph=[]

def dfs(map,x,y):
    # 주어진 범위 밖이면 즉시 종료
    if x<=-1 or x>n or y<=-1 or y>=m:
        return False
    # 현재 노드를 방문하지 않았다면
    if map[x][y]==0:
        # 방문처리
        map[x][y]=1
        # 상하좌우 위치도 모두 재귀적을 호출
        dfs(map,x-1,y)
        dfs(map,x+1,y)
        dfs(map,x,y-1)
        dfs(map,x,y+1)
        return True
    return False

for i in range(n):
    for j in range(m):
        dfs(graph,i,j)




# BFS

# BFS 구현 - 큐
from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue=deque([start])
    # 현재 노드 방문처리
    visited[start]=True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v=queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
# 각 노드가 연결된 정보를 표현 (2차원 리스트)
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
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9  # index 0을 사용하지 않기 위해 9개 선언
# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
bfs(graph, 1, visited)

# BFS 구현 - 2차원 배열
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(maze,x,y):
    queue=deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        x,y=queue.popleft()
        # 현재위치에서 4 방향으로의 위치 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #미로찾기 공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            # 괴물이 있는 경우 무시
            if maze[nx][ny]==0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if maze[nx][ny]==1:
                # 방문처리
                maze[nx][ny]=maze[x][y]+1
                queue.append((nx,ny))
    return maze[n-1][m-1]