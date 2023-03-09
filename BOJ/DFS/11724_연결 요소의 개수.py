# 연결 요소의 개수
# 방향없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램

# 입력 : 정점의 개수 n, 간선의 개수 m (1~1000, 0~n(n-1)/2)
# m개의 줄에 간선 양 끝점 u,v가 주어짐 (같은 간선은 1번씩)

# 출력: 연결요소의 개수(덩어리 수)

import sys
sys.setrecursionlimit(10000)     # dfs 런타임 에러시 추가해야함

# 입력
n,m=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# dfs 함수
def dfs(graph,v,visited):
    # 방문 처리
    visited[v]=True
    # 현재노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

# main 코드
res=0
for i in range(1,n+1):
    if not visited[i]:
        dfs(graph,i,visited)
        res+=1

print(res)

# 3 0     # 3

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