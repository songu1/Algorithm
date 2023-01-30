# 안전영역
# 물에 잠기지 않는 안전한 영역이 최대 몇개?
# 일정 높이 이하의 모든 지점은 물에 잠김

# 입력 : 지역의 열과 행의 개수 n
# 지역별 높이정보를 지도로 줌

# 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수

import sys
sys.setrecursionlimit(10000)

# 입력
n=int(sys.stdin.readline())
graph=[]
visited=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    visited.append([False]*n)

# dfs 함수
def dfs(graph,x,y,h):
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if graph[x][y]>h and not visited[x][y]:
        visited[x][y]=True
        dfs(graph,x-1,y,h)
        dfs(graph,x+1,y,h)
        dfs(graph,x,y-1,h)
        dfs(graph,x,y+1,h)
        return True
    return False

# main 코드
hmax=max(map(max,graph))
hmin=min(map(min,graph))
result=[]

for h in range(hmin,hmax):
    res=0
    for i in range(n):
        for j in range(n):
            if dfs(graph,i,j,h)==True:
                res+=1
    result.append(res)
    visited=[[False]*n for _ in range(n)]

print(max(result))




# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7           # 5

# 7
# 9 9 9 9 9 9 9
# 9 2 1 2 1 2 9
# 9 1 8 7 8 1 9
# 9 2 7 9 7 2 9
# 9 1 8 7 8 1 9
# 9 2 1 2 1 2 9
# 9 9 9 9 9 9 9       # 6

# 5
# 2 2 1 2 2
# 2 1 2 1 2
# 1 2 1 2 1
# 2 1 2 1 2
# 2 2 1 2 2           # 8

# 7
# 2 2 1 2 1 2 2
# 2 1 2 1 2 1 2
# 1 2 1 2 1 2 1
# 2 1 2 1 2 1 2
# 1 2 1 2 1 2 1
# 2 1 2 1 2 1 2
# 2 2 1 2 1 2 2       # 20