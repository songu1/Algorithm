# 바이러스
# 한 컴퓨터가 웜바이러스 걸림 -> 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터가 바이러스에 걸림
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때 1번 컴퓨터를 통해 웜바이러스에 걸리게 되는 컴퓨터의 수를 출력

# 입력 : 컴퓨터의 수 m (컴퓨터 번호 1번부터~)
# 네트워크 상에서 직접 연결된 컴퓨터 쌍의 수 n
# 네트워크 상에서 직접 연결되어있는 컴퓨터 번호 쌍 n개
# 출력 : 1번 컴퓨터가 웜바이러스에 걸렸을 때 1번 컴퓨터를 통해 웜바이러스에 걸리게 되는 컴퓨터의 수 (1번 제외)

import sys
m=int(sys.stdin.readline())
n=int(sys.stdin.readline())

graph=[[] for _ in range(1+m)]
visited=[False]*(1+m)

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


# dfs 함수
def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


dfs(graph,1,visited)
print(visited.count(True)-1) # 방문된 노드 중 1번 컴퓨터 제외하고 출력하기





# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7       # 4