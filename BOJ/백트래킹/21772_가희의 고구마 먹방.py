# 가희의 고구마 먹방
# 게임 규칙
    # 1초마다 상하좌우 방향 중 한 방향으로 1번 이동 / 머무르기
    # 이동한 지점에 고구마가 있다면 고구마 먹음
    # 고구마를 먹으면 다시 생기지 않음
    # 장애물을 뛰어 넘거나 통과할 수 없음
# 현재 위치에서 t초만큼 이동했을 때 고구마를 최대한 많이 먹으려고 함
# 최대 몇개의 고구마를 먹을 수 있는지

# 입력 : 맵의 세로r(2~100), 가로 c(2~100), 가희가 이동하는 시간 t(1~10)
# 길이가 c인 문자열 - G:가희 / S:고구마 / .:빈칸 / #:장애물
# 출력 : 문제의 답



import sys

r,c,t = map(int,sys.stdin.readline().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(r):
    graph.append(list(map(str,sys.stdin.readline().rstrip())))
    for j in range(c):
        if graph[i][j] == 'G':
            pos = (i,j)
            graph[i][j] = '.'

# 백트래킹 함수
def backtracking(num,x,y,count):
    global maxCount
    if num == t:
        maxCount = max(maxCount,count)
        return
    
    moved = False   # 현재위치에서 이동 유무를 판단하는 변수
    # 상하좌우 이동하기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c or graph[nx][ny] == "#":
            continue
        moved = True    # 이동했다고 표시
        # 빈칸으로 이동
        if graph[nx][ny] == ".":
            backtracking(num+1, nx, ny, count)
        # 고구마를 찾았다면
        elif graph[nx][ny] == "S":
            graph[nx][ny] = "."
            backtracking(num+1, nx, ny, count+1)
            graph[nx][ny] = "S"
    # 머무르는 경우
    if not moved:
        backtracking(num+1,x,y,count)

maxCount = -1
backtracking(0,pos[0],pos[1],0)
print(maxCount)

# 11 11 5
# ........G..
# ......S.#S.
# ........#.S
# ...........
# ...........
# .##########
# .##########
# ...........
# ...........
# ##########.
# ...........     # 2

# 11 11 5
# G....S.....
# ...........
# ...........
# ...........
# ...........
# ...........
# .....#.....
# ...........
# ...........
# ...........
# ...........     # 1

# 11 11 6
# .......SG..
# ........#S.
# ........#.S
# ...........
# ...........
# .##########
# .##########
# ...........
# ...........
# ##########.
# ...........     # 3

# 1차시도 틀림 : 88%
# 백트래킹 함수
# def backtracking(num,x,y,visited,count):
#     global maxCount
#     if num == t:
#         maxCount = max(maxCount,count)
#         return

#     # 상하좌우 이동하기
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or nx >= r or ny < 0 or ny >= c or graph[nx][ny] == "#":
#             continue
#         if not visited[nx][ny]:
#             # 빈칸으로 이동
#             if graph[nx][ny] == ".":
#                 visited[nx][ny] = True
#                 backtracking(num+1, nx, ny, visited, count)
#                 visited[nx][ny] = False
#             # 고구마를 찾았다면
#             elif graph[nx][ny] == "S":
#                 # reset[nx][ny] = True
#                 graph[nx][ny] = "."
#                 backtracking(num+1, nx, ny, reset, count+1)
#                 # reset[nx][ny] = False
#                 graph[nx][ny] = "S"
#     # 머무르는 경우
#     backtracking(num+1,x,y,visited,count)

# graph[pos[0]][pos[1]] = "."
# maxCount = -1
# backtracking(0,pos[0],pos[1],checked,0)