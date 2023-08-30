# 컴백홈
# 한수 위치 : 왼쪽 아래점 / 집 : 오른쪽 위
# 한번 지나친 곳은 다시 방문하지 않으면서 집으로 돌아감
# T : 가지 못하는 부분
# R*C맵에 못가는 부분과 거리 k -> 한수가 집까지 도착하는 경우 중 거리가 k인 가짓수
#       cdef  ...f  ..ef  ..gh  cdeh  cdej  ...f 
#       bT..  .T.e  .Td.  .Tfe  bTfg  bTfi  .Tde 
#       a...  abcd  abc.  abcd  a...  a.gh  abc. 
# 거리 :  6     6     6     8     8    10    6

# 입력 : r,c(1~5), k(1~r*c)
# r개줄에 맵정보를 나타내는 .과 T가 주어짐
# 출력 : 거리가 k인 가짓수

import sys

r,c,k = map(int,sys.stdin.readline().split())
graph = []
visited = [[False]*c for _ in range(r)]
for _ in range(r):
    graph.append(list(map(str,sys.stdin.readline().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def backtracking(x,y,dist):
    global count

    if x==0 and y==c-1:
        if dist == k:
            count += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=r or ny<0 or ny>=c:
            continue
        if not visited[nx][ny] and graph[nx][ny]=='.':
            visited[nx][ny] = True
            backtracking(nx,ny,dist+1)
            visited[nx][ny] = False
    return

count = 0
visited[r-1][0] = True
backtracking(r-1,0,1)
print(count)

# 3 4 6
# ....
# .T..
# ....        # 4