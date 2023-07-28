# 뱀
# 뱀이 기어다니다가 사과를 먹으면 뱀 길이가 늘어남
# n*n 정사각보드위 - 사과, 상하좌우 끝 벽
    # 뱀 (1,1)에 위치, 길이는 1, 방향은 오른쪽
# 이동 규칙
    # 몸길이를 늘릴 때 이동하려는 칸으로 늘림(머리 위치)
    # 벽 or 자기 자신의 몸과 부딪히면 게임 끝
    # 이동한 칸에 사과가 있음 -> 사과 없어짐, 머리는 사과자리, 꼬리는 움직이지 않음 
    # 이동한 칸에 사과가 없음 -> 머리는 이동한칸, 꼬리 하나 삭제
# 사과의 위치, 뱀의 이동경로 -> 이 게임이 몇초에 끝나는지 계산

# 입력 : 보드의 크기 n(2~100)
# 사과의 개수 k(0~100)
# 사과의 위치(행,열)
# 뱀의 방향 변환 횟수 L(1~100)
# 뱀의 방향 변환 정보 x초후 c방향(L:왼,D:오)으로 90도 회전 (1~10000), x가 증가하는 순
# 출력 : 게임이 몇초에 끝나는지 출력

import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
board = [[0]*(n+1) for _ in range(n+1)]   # 빈칸 : 0 , 사과 : 1, 뱀 : 9 / (1,1) ~(n,n)
board[1][1] = 9
for _ in range(k):
    x,y = map(int,sys.stdin.readline().split())
    board[x][y] = 1     # 사과
l = int(sys.stdin.readline())
dir = ['X']*10001
for _ in range(l):
    x,c = map(str,sys.stdin.readline().split())
    dir[int(x)] = c

# 상,좌,하,우 (L방향)
dx = [-1,0,1,0]
dy = [0,-1,0,1]
time = 0    # 시간(초)
queue = deque([])   # 뱀의 위치를 담은 큐
queue.append((1,1))
# 초기 머리 위치
x = 1
y = 1
# 초기 방향
d = 3
while True:
    nx = x + dx[d]
    ny = y + dy[d]
    time += 1
    # 벽을 만난 경우
    if nx < 1 or nx > n or ny < 1 or ny > n or board[nx][ny] == 9:
        break
    # 이동한 칸이 빈칸인 경우 꼬리 하나 삭제
    if board[nx][ny] == 0:
        tx,ty = queue.popleft()   # 꼬리 위치
        board[tx][ty] = 0
    # 머리 이동
    board[nx][ny] = 9
    queue.append((nx,ny))
    x = nx
    y = ny
    # 방향 전환
    if dir[time] == 'L':
        d += 1
    elif dir[time] == 'D':
        d -= 1
    if d == 4: d = 0
    elif d == -1: d = 3

print(time)

# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D        # 9

# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L        # 21

# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L        # 13