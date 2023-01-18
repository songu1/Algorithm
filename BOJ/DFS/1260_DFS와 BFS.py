# DFS와 BFS (dfs_bfs 코드, 특정 거리의 도시 찾기와 비슷)
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램 작성
# 방문할 수 있는 정점이 여러개 -> 정점 번호가 작은 것을 먼저 방문, 더 이상 방문할 점이 없으면 종료
# 정점 1번~N번
# 탐색한 결과

# 입력 : 정점 개수 N, 간선 개수 M, 탐색을 시작할 정점의 번호 V
# M개의 줄에 간선(양방향)이 연결하는 두 정점의 번호(두 정점 사이의 여러개의 간선 가능)
# 출력 : DFS 수행한 결과
# BFS 수행한 결과

import sys
from collections import deque

# 입력 및 초기화
n,m,v=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# graph 오름차순으로 sort
for i in range(n+1):
    graph[i].sort()

# dfs 함수(재귀함수/스택)
def dfs(graph,v,visited):
    visited[v]=True # 방문처리
    print(v,end=' ')
    for i in graph[v]: # 현재 노드와 연결된 다른 노드
        if not visited[i]:
            dfs(graph,i,visited)    # 재귀적으로 방문 -> DFS

# bfs 함수(큐)
def bfs(graph,start,visited):
    print('')
    queue=deque([start])       # 큐 생성
    visited[start]=True        # 방문 처리
    while queue:
        v=queue.popleft()
        print(v,end=' ')        # 큐에서 뺄 때 방문했다는 것을 출력
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

dfs(graph,v,visited)
visited=[False]*(n+1)
bfs(graph,v,visited)

# in
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# out
# 1 2 4 3
# 1 2 3 4

# in
# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1
# out
# 3 1 2 5 4
# 3 1 4 2 5

# in
# 1000 1 1000
# 999 1000
# out
# 1000 999
# 1000 999