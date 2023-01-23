# 연결 요소의 개수 - bfs가 유리!!
# 방향없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램

# 입력 : 정점의 개수 n, 간선의 개수 m
# m개의 줄에 간선 양 끝점 u,v가 주어짐 (같은 간선은 1번씩)

# 출력: 연결요소의 개수(덩어리 수)

import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# bfs 함수
def bfs(graph,start,visited):
    if visited[start]==True:
        return False
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    return True

# main 코드
res=0
for i in range(1,n+1):
    if bfs(graph,i,visited)==True:
        res+=1
print(res)

# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6     # 2

# 6 8
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 5 4
# 2 4
# 2 3        # 1

# 6 4
# 1 2
# 1 4
# 2 4
# 3 5        # 3

# 6 2
# 3 4
# 4 2         # 4

# 6 0         # 6

# 4 3
# 2 3
# 3 4
# 4 1         # 1

# 3 2
# 1 2
# 3 2         # 1

# 8 4
# 8 7
# 6 5
# 4 3
# 2 1            # 4