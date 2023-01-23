# 단지번호 붙이기 (음료수 얼려먹기와 비슷)
# 지도 1:집이 있는 곳 / 0:집이 없는곳
# 연결된 집의 모임인 단지를 정의하고 단지에 번호 붙이기
# 단지수 출력, 각 단지에 속하는 집의 수를 오름차순으로 출력

# 입력: 지도의 크기 n(정사각형)
# n개의 자료(지도)

# 출력 : 총 단지 수
# 각 단지내 집의 수를 오름차순으로 정렬

# 글로벌 함수 c 사용하여 단지별 개수 계산 -> 시간 축소 가능

import sys
from collections import deque

n=int(sys.stdin.readline())
graph=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

result=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(graph,x,y):
    queue=deque()
    if graph[x][y]!=1:
        return False
    graph[x][y]=0
    queue.append((x,y))
    count=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]==1:
                count+=1
                graph[nx][ny]=0
                queue.append((nx,ny))
    result.append(count)
    return True


# main 코드
res=0
for i in range(n):
    for j in range(n):
        if bfs(graph,i,j)==True:
            res+=1

print(res)
result.sort()
print(*result,sep='\n')

# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
# 
# 3
# 7
# 8
# 9