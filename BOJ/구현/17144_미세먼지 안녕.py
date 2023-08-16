# 미세먼지 안녕
# 집 크기 r*c 에서 각 칸에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템
# 공기청정기 1번열, 2행차지 / 공기청정기 설치되지 않은 칸은 미세먼지
# 1초 동안 일
    # 1. 미세먼지는 인접한 4방향으로 확산됨
        # 인접방향에 공기청정기가 없으면 확산 - A//5만큼 이동
        # 남은 미세먼지 : A-(A//5)*(확산된 방향의 개수)
    # 2. 공기청정기 자동
        # 공기청정기 위 : 테두리 반시계방향 순환 -> 미세먼지 바람 방향대로 한칸 이동
        # 공기청정기 아래 : 테두리 시계방향 순환 -> 미세먼지 바람 방향대로 한칸 이동
        # 공기청정기로 미세먼지 들어감
# 방 정보 -> t초가 지난 후 방에 남아있는 미세먼지 양

# 입력 : r,c(6~50), t(1~1000)
# 미세먼지양 a (공기청정기 위치는 -1)
# 출력 : t초가 지난 후 방에 남아있는 미세먼지 양

import sys

r,c,t = map(int,sys.stdin.readline().split())
room = []
for i in range(r):
    room.append(list(map(int,sys.stdin.readline().split())))
    for j in range(c):
        if room[i][j] == -1:
            posX, posY = i,j
            break

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 미세먼지 확산 함수
def moveDust(room):
    dust = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if room[x][y] == 0:
                continue
            dust[x][y] += room[x][y]
            if room[x][y] != -1:
                amount = room[x][y] // 5
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx<0 or nx>=r or ny<0 or ny>=c or room[nx][ny]==-1:
                        continue
                    dust[nx][ny] += amount
                    dust[x][y] -= amount
    return dust

# 공기청정기 가동(위) 함수 (posX-1,0)
def upperMachine(room):
    # (_, 0)
    for i in range(posX-2,0,-1):
        room[i][0] = room[i-1][0]
    # (0, _)
    for i in range(c-1):
        room[0][i] = room[0][i+1]
    # (_, c-1)
    for i in range(posX-1):
        room[i][c-1] = room[i+1][c-1]
    # (a-1, _)
    for i in range(c-1,1,-1):
        room[posX-1][i] = room[posX-1][i-1]
    room[posX-1][1] = 0


# 공기청정기 가동(아래) 함수 (posX,0)
def lowerMachine(room):
    # (_, 0)
    for i in range(posX+1,r-1):
        room[i][0] = room[i+1][0]
    # (r-1, _)
    for i in range(c-1):
        room[r-1][i] = room[r-1][i+1]
    # (_, c-1)
    for i in range(r-1,posX,-1):
        room[i][c-1] = room[i-1][c-1]
    # (posX, _)
    for i in range(c-1,1,-1):
        room[posX][i] = room[posX][i-1]
    room[posX][1] = 0

for _ in range(t):
    # 미세먼지 확산
    room = moveDust(room)
    # 공기청정기 가동(위)
    upperMachine(room)
    # 공기청정기 가동(아래)
    lowerMachine(room)

result = 0
for i in range(r):
    result += sum(room[i])
print(result+2)



# 7 8 1
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0           # 188

# 7 8 2
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0           # 188

# 7 8 3
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0           # 186

# 7 8 4
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0           # 178

# 7 8 5
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0           # 172

# 7 8 20
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0           # 71

# 7 8 30
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0           # 52

# 7 8 50
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0           # 46