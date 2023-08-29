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
sys.setrecursionlimit(1000000)

line = []
v,e = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
visited = [0]*(v+1)
for _ in range(e):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 함수
def dfs(graph,v,pre):
    global num
    num += 1
    visited[v] = num
    minOrder = visited[v]
    for i in graph[v]:
        # 바로 직전값은 제외
        if i == pre:
            continue
        if not visited[i]:
            order = dfs(graph,i,v)
            if order > visited[v]:
                if v>i:
                    result.append((i,v))
                else:
                    result.append((v,i))
            minOrder = min(minOrder, order)
        else:
            minOrder = min(minOrder, visited[i])
    return minOrder

num = 0
rootChild = 0
result = []
dfs(graph,1,-1)
result.sort()
print(len(result))
for res in result:
    print(*res,sep=" ")


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