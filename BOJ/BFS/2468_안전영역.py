# 안전영역 - BFS 사용 시 DFS보다 메모리는 살짝 크고 시간은 적음
# 물에 잠기지 않는 안전한 영역이 최대 몇개?
# 일정 높이 이하의 모든 지점은 물에 잠김

# 입력 : 지역의 열과 행의 개수 n(2~100)
# 지역별 높이정보를 지도로 줌 (1~100)

# 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수

import sys
from collections import deque

# 입력
n=int(sys.stdin.readline())
graph=[]
visited=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    visited.append([False]*n)

# bfs 함수
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(graph,x,y,h):
    # 방문처리
    visited[x][y]=True
    # 잠기는 영역이면 BFS X
    if graph[x][y]<=h:
        return False
    queue=deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            # 잠기지 않는 영역이며 아직 방문하지 않았으면 방문
            if graph[nx][ny]>h and not visited[nx][ny]:
                queue.append((nx,ny))
            visited[nx][ny]=True
    return True



# main 코드
hmax=max(map(max,graph))
hmin=min(map(min,graph))
result=[]

for h in range(hmin-1,hmax+1):
    res=0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(graph,i,j,h)==True:
                    res+=1
    result.append(res)
    visited=[[False]*n for _ in range(n)]

print(max(result))







# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7           # 5

# 7
# 9 9 9 9 9 9 9
# 9 2 1 2 1 2 9
# 9 1 8 7 8 1 9
# 9 2 7 9 7 2 9
# 9 1 8 7 8 1 9
# 9 2 1 2 1 2 9
# 9 9 9 9 9 9 9       # 6

# 5
# 2 2 1 2 2
# 2 1 2 1 2
# 1 2 1 2 1
# 2 1 2 1 2
# 2 2 1 2 2           # 8

# 7
# 2 2 1 2 1 2 2
# 2 1 2 1 2 1 2
# 1 2 1 2 1 2 1
# 2 1 2 1 2 1 2
# 1 2 1 2 1 2 1
# 2 1 2 1 2 1 2
# 2 2 1 2 1 2 2       # 20

# 2
# 1 1
# 1 1                 # 1