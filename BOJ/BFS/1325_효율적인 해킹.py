# 효율적인 해킹
# n개의 컴퓨터, 한번의 해킹 -> 여러개의 컴퓨터 해킹
# a -> b 신뢰 : b 해킹시 a도 해킹 (일방향)

# 입력 : n,m
# m개의 줄에 신뢰하는 관계 a,b (1~n) : a-> b
# 출력 : 김지민이 한번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터 번호를 오름차순으로

# 1차 시도 : dfs 시간초과 (일반 dfs)
# 2차 시도 : dfs 1%에서 틀림 -> dp로 풀면 겹칠 수 있음 ex) 1->2,4->3,4
# 3차 시도 : bfs : python3로는 실패, pypy3로는 성공

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]    # b인덱스에 a넣기
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[b].append(a)

# dfs 함수
def dfs(graph,v,visited):
    global count
    visited[v] = True
    if len(graph[v]) == 0:
        return
    # count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            count += 1
# bfs 함수
def bfs(graph,v,visited):
    global count
    queue = deque([])
    visited[v] = True
    count += 1
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                count += 1
                queue.append(i)

maxCount = 0
result = [0]
# main 코드
for i in range(1,n+1):
    count = 0
    visited = [False]*(n+1)
    # dfs(graph,i,visited)
    bfs(graph,i,visited)
    maxCount = max(maxCount, count)
    result.append(count)

for i in range(1,n+1):
    if result[i] == maxCount:
        print(i,end=" ")


# 5 4
# 3 1
# 3 2
# 4 3
# 5 3     # 1 2