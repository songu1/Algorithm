# 청소년 상어
# 4*4크기 공간 좌표의 각 칸에 물고기가 한마리 존재
# 물고기는 번호(1~16), 방향(상하좌우,대각선)을 가짐 (번호는 겹칠 수 없음)
# (1) 청소년 상어 (0,0)의 물고기를 먹고 (0,0)에 들어감
    # 상어의 방향 : (0,0) 물고기의 방향과 같음
# (2) 물고기 번호가 작은 물고기부터 순서대로 한칸 이동
        # 빈칸 : 이동
        # 다른 물고기가 있는 칸 : 서로의 위치를 바꿈
        # 상어 or 공간 밖 : 이동 불가
    # 방향으로 이동할 수 없다면 이동할수 있을 때까지 45도 반시계 회전 (물고기 방향이 바뀜)
    # 방향을 찾으면 이동 / 그래도 없으면 이동 X
# (3) 상어 : 방향에 있는 칸으로 한번에 여러개 칸 이동 가능
        # 물고기 있는 칸 : 물고기 먹고 물고기 방향 가짐
        # 물고기 없는 칸 : 이동 불가
    # 지나가는 칸 : 물고기 먹지 않음 
    # 방향에 있는 칸 중 물고기가 있는 칸 중 하나로 이동
# (2),(3) 반복
# 상어 이동 가능 칸이 없으면 집으로감
# 상어가 먹을 수 있느 물고기 번호의 합의 최댓값

# 입력 : 각 칸에 들어있는 물고기 정보 - 물고기 번호 ai(1~16), 물고기 방향 bi(1~8)
# 출력 : 상어가 먹을 수 있는 물고기 번호의 합이 최댓값

import sys

# 입력
fish = [[] for _ in range(4)]       # 상어는 [0,방향] , 물고기는 [1~16,방향], 빈칸은 [99,99]
fishLoc = [() for _ in range(17)]   # 각 물고기의 x,y좌표 (물고기가 없다면 빈 튜플)
for i in range(4):
    input = list(map(int,sys.stdin.readline().split()))
    for j in range(4):
        fish[i].append([input[2*j], input[2*j+1]])
        fishLoc[input[2*j]]=(i,j)

dx = [9,-1,-1,0,1,1,1,0,-1]
dy = [9,0,-1,-1,-1,0,1,1,1]

# 물고기 이동 함수
def moveFish(fish,fishLoc):
    for i in range(1,17):
        if fishLoc[i] == ():
            continue
        x,y = fishLoc[i]
        d = fish[x][y][1]   # 물고기 방향
        for _ in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            
            # 공간 안이고 상어가 존재하지 않는 경우
            if 0<=nx<4 and 0<=ny<4 and fish[nx][ny][0] != 0:
                # 빈칸이면 fish 위치 변경
                if fish[nx][ny] == [99,99]:
                    fishLoc[i] = (nx,ny)
                # 다른 물고기라면 fish 위치 교환
                else:
                    fishLoc[i],fishLoc[fish[nx][ny][0]] = fishLoc[fish[nx][ny][0]], fishLoc[i]
                # 물고기 방향, 위치 변경
                fish[x][y][1] = d   # 현재 물고기의 방향을 변경
                fish[x][y], fish[nx][ny] = fish[nx][ny], fish[x][y] # 물고기의 위치를 교환/변경
                break
            if d == 8: d = 1
            else: d += 1

# 백트래킹
def backtracking(fish,fishLoc,x,y,arr):
    global maxSum
    # 상어가 먹음
    fishLoc[fish[x][y][0]] = ()
    fish[x][y][0] = 0
    # 물고기 이동
    moveFish(fish,fishLoc)
    # 상어 이동
    d = fish[x][y][1]   # 상어 방향
    fish[x][y] = [99,99]     # 상어 위치는 빈칸이 됨
    for i in range(1,4):
        nx = x + dx[d]*i
        ny = y + dy[d]*i
        if nx<0 or nx>=4 or ny<0 or ny>=4:
            break
        if fish[nx][ny] != [99,99]:
            fish2 = [[f2[:] for f2 in f1] for f1 in fish]
            backtracking(fish2,fishLoc[:],nx,ny,arr + [fish[nx][ny][0]])

    maxSum = max(maxSum,sum(arr))
    return


# main 코드
maxSum=0
backtracking(fish,fishLoc,0,0,[fish[0][0][0]])
print(maxSum)


# 7 6 2 3 15 6 9 8
# 3 1 1 8 14 7 10 1
# 6 1 13 6 4 3 11 4
# 16 1 8 7 5 2 12 2       # 33

# 16 7 1 4 4 3 12 8
# 14 7 7 6 3 4 10 2
# 5 2 15 2 8 3 6 4
# 11 8 2 4 13 5 9 4       # 43

# 12 6 14 5 4 5 6 7
# 15 1 11 7 3 7 7 5
# 10 3 8 3 16 6 1 1
# 5 8 2 7 13 6 9 2        # 76

# 2 6 10 8 6 7 9 4
# 1 7 16 6 4 2 5 8
# 3 7 8 6 7 6 14 8
# 12 7 15 4 11 3 13 3     # 39