# 단절선
# 그래프 -> 단절선을 모두 구해 출력
# 단절선 : 그 간선을 제거햇을 때, 그래프가 2개 또는 그 이상으로 나누어지는 간선
# 제거했을 때 그래프의 connected componenet 개수가 증가하는 간선

# 입력 : 정점 개수 v(1~100,000) , 간선 개수 e(1~1,000,000)
# e개의 줄에 간선 정보 a,b (양방향 연결)
    # 그래프 항상 연결됨, 같은 간선은 1번만
    # 정점은 1~V
# 출력 : 단절선의 개수 k
# k개의 줄에 단절선을 중복없이 사전순으로 출력 : "A B" 형식(A<B)

import sys

line = []
v,e = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)

# DFS 함수
def dfs(graph,v,start,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,v,start,visited)
    return

# result = []
# for i in range(1,v+1):
#     visited = [False]*(v+1)
#     dfs(graph,graph[i][0],i,visited)
#     for j in range(1,v+1):
#         if visited[j] == False:
            
#     if visited.count(False) > 1:
#         result.append()


# 7 8
# 1 4
# 4 5
# 5 1
# 1 6
# 6 7
# 2 7
# 7 3
# 2 3
# #
# 2
# 1 6
# 6 7