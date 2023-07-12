# 아기 상어
# n*n 크기의 공간 : 물고기 m마리, 아기 상어 1마리 (1칸에는 물고기 최대 1마리)
# 아기 상어, 물고기 : 크기를 가짐(자연수)
# 아기상어 : 초기 크기 2
    # 1초 상하좌우 한칸 이동, 물고기 먹으면 그 칸은 빈칸
    # 아기상어 크기 > 물고기 크기 : 먹을 수 O, 지나갈 수 O
    # 아기상어 크기 == 물고기 크기 : 지나갈 수 O
    # 아기상어 크기 < 물고기 크기 : 다 안됨
# 이동 방법
    # 더 이상 먹을 수 있는 물고기 X : 엄마 상어에게 도움 요청
    # 먹을 수 있는 물고기가 1마리 -> 그 물고기
    # 여러개 -> 가장 가까운 물고기(도달하기 위해 지나가야하는 칸의 최소 수)
        # 거리 같으면 -> 가장 위, 가장 왼쪽 물고기가 우선
# 자신의 크기와 같은 수의 물고기를 먹으면 크기가 1씩 증가
# 공간의 상태 -> 아기 상어가 몇초동안 엄마상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지

# 입력 : 공간의 크기 n(2~20)
# 공간의 상태
    # 0 : 빈칸s
    # 1,2,3,4,5,6 : 물고기 크기
    # 9 : 아기 상어 위치
# 출력 : 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간

# 2차시도 : 성공 -> 이미 탐색한 위치를 visited 배열로 체크해줌, 물고기를 잡아먹으면 visited 배열 초기화
import sys
import heapq

n = int(sys.stdin.readline())
area=[]
fish = []
for i in range(n):
    area.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        if area[i][j] == 9:
            posX = i
            posY = j
        elif area[i][j] != 0:
            fish.append(area[i][j])
fish.sort()
visited = [[False]*n for _ in range(n)]

dx=[-1,0,0,1]
dy=[0,-1,1,0]
# bfs 함수
def bfs(area,x,y,visited):
    q = []
    size = 2    # 아기 상어 크기
    count= 0    # 상어 크기가 바뀐 후 잡아먹은 물고기 수
    time = 0    # 시간
    area[x][y] = 0
    visited[x][y] = True
    heapq.heappush(q,(0,x,y))
    while q:
        lev,x,y = heapq.heappop(q)
        # 물고기를 잡아먹는 경우
        if 0 < area[x][y] < size:
            time = lev
            count += 1  # 물고기 수 count
            if count == size:   # 상어 크기 증가
                size += 1
                count = 0
            fish.remove(area[x][y])
            if len(fish)==0 or fish[0] >= size: # 남은 물고기를 더이상 먹을수 없다면 return
                return time
            area[x][y] = 0
            q = []
            visited = [[False]*n for _ in range(n)]
            visited[x][y] = True
        # 주변 탐색
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if area[nx][ny] <= size and not visited[nx][ny]:
                heapq.heappush(q,(lev+1,nx,ny))
                visited[nx][ny] = True
    return time

if len(fish) == 0:
    print(0)
else:
    print(bfs(area,posX,posY,visited))

# 1차 시도 -> 3%에서 시간초과 : 이동할 때 이미 방문한 노드를 재방문하지 않도록 해야하는데 이를 (lev+1,nx,ny) not in q와 (nx,ny) != pre 로 설정하여 오래걸림
# import sys
# import heapq

# n = int(sys.stdin.readline())
# area=[]
# fish = []
# for i in range(n):
#     area.append(list(map(int,sys.stdin.readline().split())))
#     for j in range(n):
#         if area[i][j] == 9:
#             posX = i
#             posY = j
#         elif area[i][j] != 0:
#             fish.append(area[i][j])
# fish.sort()

# dx=[-1,0,0,1]
# dy=[0,-1,1,0]
# # bfs 함수
# def bfs(area,x,y):
#     q = []
#     size = 2    # 아기 상어 크기
#     count= 0    # 상어 크기가 바뀐 후 잡아먹은 물고기 수
#     time = 0    # 시간
#     pre = (-2,-2)   # 이전 위치(이동 시 다시 가지 않기 위해)
#     area[x][y] = 0
#     heapq.heappush(q,(0,x,y))
#     while q:
#         lev,x,y = heapq.heappop(q)
#         # 물고기를 잡아먹는 경우
#         if area[x][y]<size and area[x][y]>0:
#             time = lev
#             count += 1  # 물고기 수 count
#             if count == size:   # 상어 크기 증가
#                 size += 1
#                 count = 0
#             fish.remove(area[x][y])
#             if len(fish)==0 or fish[0] >= size: # 남은 물고기를 더이상 먹을수 없다면 return
#                 return time
#             area[x][y] = 0
#             q = []
#             pre = (-2,-2)
#         # 주변 탐색
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx<0 or nx>=n or ny<0 or ny>=n:
#                 continue
#             if (lev+1,nx,ny) not in q and area[nx][ny] <= size and (nx,ny) != pre:
#                 heapq.heappush(q,(lev+1,nx,ny))
#         pre = (x,y)
#     return time

# if len(fish) == 0:
#     print(0)
# else:
#     print(bfs(area,posX,posY))


# 3
# 0 0 0
# 0 0 0
# 0 9 0           # 0

# 3
# 0 0 1
# 0 0 0
# 0 9 0           # 3

# 4
# 4 3 2 1
# 0 0 0 0
# 0 0 9 0
# 1 2 3 4         # 14

# 6
# 5 4 3 2 3 4
# 4 3 2 3 4 5
# 3 2 9 5 6 6
# 2 1 2 3 4 5
# 3 2 1 6 5 4
# 6 6 6 6 6 6     # 60

# 6
# 6 0 6 0 6 1
# 0 0 0 0 0 2
# 2 3 4 5 6 6
# 0 0 0 0 0 2
# 0 2 0 0 0 0
# 3 9 3 0 0 1     # 48

# 6
# 1 1 1 1 1 1
# 2 2 6 2 2 3
# 2 2 5 2 2 3
# 2 2 2 4 6 3
# 0 0 0 0 0 6
# 0 0 0 0 0 9     # 39

# 7
# 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1
# 1 1 1 1 1 1 9

# 6
# 1 2 0 3 1 6
# 1 0 5 0 0 0
# 1 0 2 0 2 0
# 0 1 4 0 2 5
# 6 6 3 0 3 3
# 4 9 6 0 2 2   # 0