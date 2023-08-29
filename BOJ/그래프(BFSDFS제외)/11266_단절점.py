# 단절점 - 힌트 보고 풂
# DFS spanning tree
# 그래프가 주어졌을 때 단절점을 모두 구해 출력하는 프로그램
# 단절점 : 정점을 제거했을 때 그래프가 2개 또는 그 이상으로 나누어지는 정점

# 입력 : 정점 개수 v(1~100,000) , 간선 개수 e(1~1,000,000)
# e개의 줄에 간선 정보 a,b (양방향 연결)
    # 주어지는 그래프 연결 그래프가 아닐수도 있음
    # 정점은 1~V
# 출력 : 단절점의 개수
# 단절점으 ㅣ번호(공백)

# 1차시도 실패 : 주어지는 그래프가 연결 그래프가 아닐 경우를 생각하지 못함
# 2차시도 성공 : 방문하지 않은 경우에 대해 dfs를 수행

import sys
sys.setrecursionlimit(1000000)

line = []
v,e = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
visited = [0]*(v+1)
for _ in range(e):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

# dfs 함수
def dfs(graph,v,root):
    global num, rootPath
    num+=1
    visited[v] = num
    minOrder = num
    point=False
    for i in graph[v]:
        # 방문하지 않은 노드만 dfs함수 수행
        if not visited[i]:
            # root노드의 인접정점의 수 count
            if root:
                rootPath += 1
            order = dfs(graph,i,False)
            if not root and order >= visited[v]:
                point = True
            minOrder = min(minOrder,order)
        else:
            minOrder = min(minOrder, visited[i])
    if point:
        result.append(v)
    return minOrder

num = 0
rootPath = 0
result=[]
for i in range(1,v+1):
    if not visited[i]:
        dfs(graph,i,True)
        # 루트노드의 정점이 2개 이상인 경우
        if rootPath >= 2:
            result.append(i)
        rootPath = 0
# print(visited)
result.sort()
print(len(result))
print(*result,sep=" ")

# 7 7
# 1 4
# 4 5
# 5 1
# 1 6
# 6 7
# 2 7
# 7 3
# #
# 3
# 1 6 7

# 7 7
# 1 2
# 2 3
# 3 4
# 4 6
# 6 5
# 7 4
# 7 1
# #
# 2
# 4 6

# 20 15
# 6 2
# 16 1
# 6 1
# 14 3
# 20 19
# 8 17
# 3 7
# 1 9
# 14 20
# 2 20
# 19 7
# 2 16
# 11 8
# 6 18
# 15 11
# #
# 6
# 1 2 6 8 11 20