# 트리의 부모 찾기
# 루트 없는 트리가 주어짐 (루트 : 1)
# 각 노드의 부모를 구하는 프로그램

# 입력 : 노드의 개수(2~100,000)
# n-1줄에 트리 상에서 연결된 두 정점이 주어짐
# 출력 : 첫째줄부터 n-1개의 줄에 각 노드의 부모 노드 번호를 2번 노트부터 출력

import sys
sys.setrecursionlimit(1000000)
# 입력
n=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
parent=[-1]*(n+1)
for i in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

# dfs함수
def dfs(v,parent):
    # 인접 노드
    for i in graph[v]:
        if parent[i]==-1:
            parent[i]=v
            dfs(i,parent)
    return parent

# main
parent[1]=0
parent=dfs(1,parent)
for i in range(2,len(parent)):
    print(parent[i])

# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7
# 
# 4
# 6
# 1
# 3
# 1
# 4

# 12
# 1 2
# 1 3
# 2 4
# 3 5
# 3 6
# 4 7
# 4 8
# 5 9
# 5 10
# 6 11
# 6 12
#
# 1
# 1
# 2
# 3
# 3
# 4
# 4
# 5
# 5
# 6
# 6