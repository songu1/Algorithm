# 섬의 개수 - dfs, bfs 모두 가능
# 가로, 세로, 대각선으로 이동 가능
# 같은 섬 : 걸어서 갈 수 있는 경로가 있어야함
# 지도는 바다로 둘러싸여있어 지도밖으로 나갈 수 없음
# 1: 땅, 0: 바다

# 입력 : 여러개의 테스트 케이스
# 지도의 너비 w와 높이 h ( w,h <=50 )
# h개의 줄에 지도
# 다음 테스트 케이스...
# 입력 마지막줄 0 0

# 각 테스트 케이스의 섬의 개수

import sys
from collections import deque

def bfs(graph,x,y):
    if graph[x][y]==0:
        return False
    dx=[-1,-1,0,1,1,1,0,-1]
    dy=[0,1,1,1,0,-1,-1,-1]
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=h or ny>=w:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
    return True

result=[]
while True:
    # 입력
    w,h=map(int,sys.stdin.readline().split())
    if w==0 and h==0:
        break
    graph=[]
    for i in range(h):
        graph.append(list(map(int,sys.stdin.readline().split())))
# main 코드
    res=0
    for i in range(h):
        for j in range(w):
            if bfs(graph,i,j)==True:
                res+=1
    result.append(res)
    

print(*result,sep='\n')




# 1 1
# 0
# 2 2
# 0 1
# 1 0
# 3 2
# 1 1 1
# 1 1 1
# 5 4
# 1 0 1 0 0
# 1 0 0 0 0
# 1 0 1 0 1
# 1 0 0 1 0
# 5 4
# 1 1 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 1 1
# 5 5
# 1 0 1 0 1
# 0 0 0 0 0
# 1 0 1 0 1
# 0 0 0 0 0
# 1 0 1 0 1
# 0 0
#
# 0
# 1
# 1
# 3
# 1
# 9