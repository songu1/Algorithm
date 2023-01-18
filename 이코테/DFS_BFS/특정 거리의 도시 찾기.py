# 339p
# 1~n번까지의 도시, M개의 단방향 도로(거리 1)
# 특정 도시 X 출발하여 도달할 수 있는 모든 도시 중 최단거리가 K인 모든 도시 번호를 출력
# 자기자신 이동 - 0

# 도시개수 N, 도로개수 M, 거리 정보 K, 출발 도시번호 X
# M개의 줄에 걸려 자연수 A,B(공백 구분) : A->B 도로

# 최단거리가 k인 모든 도시 번호를 한줄에 하나씩 오름차순으로 출력
# 없으면 -1 출력

# BFS

import sys
from collections import deque

graph=[]

# 입력받아 그래프 만들기
n,m,k,x=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)

visited=[-1]*(n+1)       # (-1) -1 -1 -1 -1

# bfs 생성
def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=0
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if visited[i]==-1:
                queue.append(i)
                visited[i]=visited[v]+1
    return visited


# main 코드
visited=bfs(graph,x,visited)
if k in visited:
    for i in range(1,len(visited)):
        if visited[i]==k:
            print(i)
else:
    print(-1)


# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4         # 4

# 4 3 2 1
# 1 2
# 1 3
# 1 4         # -1

# 4 4 1 1
# 1 2
# 1 3
# 2 3
# 2 4
# 답
# 2
# 3