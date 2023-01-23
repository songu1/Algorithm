# 유기농 배추 - dfs가 더 알맞음
# 배추 흰지렁이 인접한 배추로 이동가능 -> 인접한 배추도 보호받을 수 있음
#
# 입력: 테스트 케이스 수 T
# 각각의 테스트 케이스에 대해
    # 배추밭의 가로길이 M, 배추밭의 세로길이 N, 배추가 심어져있는 위치의 개수 k
    # 배추의 위치 X, Y

# 출력 : 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리수

import sys
from collections import deque

result=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(graph,y,x):
    queue=deque()
    queue.append((y,x))
    if graph[y][x]==0:
        return False
    graph[y][x]=0
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            if graph[ny][nx]==1:
                graph[ny][nx]=0
                queue.append((ny,nx))

    return True

t=int(sys.stdin.readline())
for _ in range(t):
    m,n,k=map(int,sys.stdin.readline().split())
    graph=[[0]*m for _ in range(n)]
    for _ in range(k):
        x,y=map(int,sys.stdin.readline().split())
        graph[y][x]=1
    # bfs
    res=0
    for i in range(n):      # y
        for j in range(m):  # x
            if bfs(graph,i,j)==True:
                res+=1
    result.append(res)

print(*result,sep='\n')


# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5
#
# 5
# 1

# 1
# 5 3 6
# 0 2
# 1 2
# 2 2
# 3 2
# 4 2
# 4 0     # 2