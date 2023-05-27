# 촌수계산
# 촌수 (부모-자식 : 1촌)기준
# 여러 사람들에 대한 부모 자식 간의 관계 -> 두 사람의 촌수를 계산하는 프로그램
# 사람 : 1,2,3,..,n (1~100)의 연속된 번호 / 부모는 1명만 주어짐

# 입력 : 전체 사람 수 n
# 촌수를 계산해야하는 서로 다른 두 사람 번호
# 부모 자식간의 관계 개수 m
# 부모 자식 관계를 나타내는 두 번호 x(부모),y(자식)
# 출력 : 요구한 두 사람의 촌수를 나타내는 정수, 촌수를 계산할 수 없다면 -1 출력

import sys

# 입력
n = int(sys.stdin.readline())
a,b = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
visited=[-1]*(n+1)

# dfs 함수
def dfs(graph,x,visited):
    # 촌수를 찾은 경우
    if x==b:
        return 
    # 탐색
    for v in graph[x]:
        if visited[v]==-1:
            visited[v]=visited[x]+1
            dfs(graph,v,visited)

# main 코드
visited[a]=0
dfs(graph,a,visited)
print(visited[b])


# 9
# 7 3
# 7
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6         # 3

# 9
# 8 6
# 7
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6     # -1