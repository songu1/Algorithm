# 치즈
# n*m의 모눈 종이 위에 얇은 치즈가 표시
# 치즈를 실내온도에 내어놓으면 천천히 녹음
# 각 치즈 격자의 4변 중 2변 이상이  외부공간과 접촉 -> 한시간만에 녹아 없어짐
    # 치즈 내부에 있는 공간은 해당 안됨
# 모눈 종이의 맨 가장자리는 치즈가 놓이지 않음
# 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간

# 입력 : 모눈종이 크기 n,m(5~100)
# 모눈 종이 치즈 모양 (치즈 : 1 / 치즈X : 0)
# 출력 : 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간



# 1차 시도 - 통과 (34184KB / 1272ms)

# import sys
# from collections import deque

# n,m = map(int,sys.stdin.readline().split())
# graph = []
# cheese = []
# for i in range(n):
#     graph.append(list(map(int,sys.stdin.readline().split())))
#     for j in range(m):
#         if graph[i][j] == 1:
#             cheese.append((i,j))

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# # bfs 함수 : 외부 공간 체크
# def bfs(graph,x,y):
#     queue = deque([])
#     graph[x][y] = -1
#     queue.append((x,y))
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx<0 or nx>=n or ny<0 or ny>=m:
#                 continue
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = -1
#                 queue.append((nx,ny))

# time = 0
# while len(cheese) > 0:
#     time += 1
#     # 치즈 외부공간 체크
#     bfs(graph,0,0)
#     # 치즈 녹음
#     for k in range(len(cheese)-1,-1,-1):
#         count = 0
#         for i in range(4):
#             nx = cheese[k][0] + dx[i]
#             ny = cheese[k][1] + dy[i]
#             if nx<0 or nx>=n or ny<0 or ny>=m:
#                 continue
#             if graph[nx][ny] == -1:
#                 count += 1
#         if count >= 2:
#             del cheese[k]
#     # 치즈 초기화
#     graph = [[0]*m for _ in range(n)]
#     for c in cheese:
#         graph[c[0]][c[1]] = 1

# print(time)

# 2차 시도 : 통과 (34216KB / 820ms) - 시간 줄임

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = []
cheese = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    for j in range(m):
        if graph[i][j] == 1:
            cheese.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# bfs 함수 : 외부 공간 체크
def bfs(graph,x,y):
    queue = deque([])
    graph[x][y] = -1
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = -1
                queue.append((nx,ny))

time = 0
# 치즈 외부공간 체크
bfs(graph,0,0)
while len(cheese) > 0:
    time += 1
    melted = []
    # 치즈 녹음
    for k in range(len(cheese)-1,-1,-1):
        count = 0
        x = cheese[k][0]
        y = cheese[k][1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == -1:
                count += 1
        if count >= 2:
            melted.append(cheese[k])
            del cheese[k]
    # 녹은 치즈 외부 공간으로 바꾸기
    for melt in melted:
        graph[melt[0]][melt[1]] = -1
        bfs(graph,melt[0],melt[1])

print(time)


# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 1 1 0 0 0 0
# 0 0 0 1 1 0 1 1 0
# 0 0 1 1 1 1 1 1 0
# 0 0 1 1 1 1 1 0 0
# 0 0 1 1 0 1 1 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0       # 4

# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 1 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 0 0 1 0 0 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 1 0 0 0 1 1 0
# 0 0 0 0 0 0 0 0 0         # 3