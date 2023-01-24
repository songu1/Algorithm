# 숨바꼭질
# 수빈이 위치 N, 동생 위치 k (0<=n,k<=100000)
# 걷기 : x-1, x+1
# 순간이동 : 2*x
# 수빈, 동생 위치 -> 수빈이가 동생을 찾을 수 있는 가장 빠른 시간

# 입력 : 수빈위치 n, 동생 위치 k
# 출력 : 동생을 찾는 가장 빠른 시간

# 값은 100000을 넘기면 안됨 -> 생각해서 풀기(아니면 런타임에러)

import sys
from collections import deque

def bfs(graph,n,k,visited):
    queue=deque()
    queue.append(n)
    visited[n]=True
    while queue:
        v=queue.popleft()
        dx=[-1,1,v]
        for i in range(3):
            nx=v+dx[i]
            if nx<0 or nx>100000:
                continue
            if not visited[nx]:
                graph[nx]=graph[v]+1
                queue.append(nx)
                visited[nx]=True
    return graph[k]

# 입력
n,k=map(int,sys.stdin.readline().split())
graph=[0]*100001
visited=[False]*100001

# main 코드
print(bfs(graph,n,k,visited))



# 5 17      # 4
# 5 8       # 2
# 2 1       # 1 - 이상
# 2 0       # 2 - 이상
# 0 1       # 1 - 이상
# 1 3       # 2