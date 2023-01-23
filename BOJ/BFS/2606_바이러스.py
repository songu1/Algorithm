# 바이러스
# 한 컴퓨터가 웜바이러스 걸림 -> 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터가 바이러스에 걸림
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때 1번 컴퓨터를 통해 웜바이러스에 걸리게 되는 컴퓨터의 수를 출력

# 입력 : 컴퓨터의 수 m (컴퓨터 번호 1번부터~)
# 네트워크 상에서 직접 연결된 컴퓨터 쌍의 수 n
# 네트워크 상에서 직접 연결되어있는 컴퓨터 번호 쌍 n개
# 출력 : 1번 컴퓨터가 웜바이러스에 걸렸을 때 1번 컴퓨터를 통해 웜바이러스에 걸리게 되는 컴퓨터의 수 (1번 제외)

import sys
from collections import deque

m=int(sys.stdin.readline())
n=int(sys.stdin.readline())
graph=[[] for _ in range(m+1)]
visited=[False]*(m+1)

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

# main 코드
bfs(graph,1,visited)
print(visited.count(True)-1)

# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7       # 4