# 나이트의 이동
# 나이트가 한번에 이동할 수 있는 칸 : +-2, +=1
# 나이트가 이동하려는 칸 -> 몇번 움직이면 이 칸으로 이동할 수 있는지

# 입력 : 테스트케이스 수
# 각 테스트 케이스 3줄
    # 체스판 한 변의 길이 l (4~300)
    # 현재 나이트 칸
    # 나이트가 이동하려는 칸
# 출력 : 각 테스트 케이스마다 나이트가 최소 몇번만에 이동가능한지

import sys
from collections import deque

tc=int(sys.stdin.readline())
result=[]

dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]
for _ in range(tc):
    # 입력
    l=int(sys.stdin.readline())
    x,y=map(int,sys.stdin.readline().split())
    a,b=map(int,sys.stdin.readline().split())
    graph=[[-1]*l for _ in range(l)]

    # bfs
    queue=deque()
    queue.append((x,y))
    # 방문처리
    graph[x][y]=0
    while queue:
        x,y=queue.popleft()
        if x==a and y==b:
            result.append(graph[x][y])
            break
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=l or ny<0 or ny>=l:
                continue
            if graph[nx][ny]==-1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))

print(*result,sep="\n")


# 3
# 8
# 0 0
# 7 0
# 100
# 0 0
# 30 50
# 10
# 1 1
# 1 1
#
# 5
# 28
# 0
