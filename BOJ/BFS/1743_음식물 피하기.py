# 음식물 피하기
# 음식물이 통로 중간중간에 떨어져 있음 / 근처에 있는 것끼리 뭉쳐 큰 음식물 쓰레기가 됨
# 선생님은 떨어진 음식물 중에 제일 큰 음식물만 피해가려고함
# 제일 큰 음식물의 크기를 구하기

# 입력 : 통로의 세로길이 n, 가로길이 m (1~100), 음식물 쓰레기 개수 k(1~n*m)
# 음식물이 떨어진 좌표 (r,c)
# 출력 : 음식물 중 가장 큰 음식물의 크기

# bfs
import sys
from collections import deque

n,m,k = map(int,sys.stdin.readline().split())
graph=[['.']*m for _ in range(n)]
for _ in range(k):
    r,c = map(int,sys.stdin.readline().split())
    graph[r-1][c-1] = '#'

# bfs
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(graph,x,y):
    queue = deque([])
    # 방문처리
    graph[x][y] = '*'
    count = 1
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == '#':
                graph[nx][ny] = '*'
                count += 1
                queue.append((nx,ny))
    return count

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '#':
            result = max(bfs(graph,i,j),result)

print(result)

# 3 4 5
# 3 2
# 2 2
# 3 1
# 2 3
# 1 1         # 4