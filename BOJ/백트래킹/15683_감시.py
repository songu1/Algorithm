# 감시
# n*m 크기의 지도 : 0 빈칸, 6 벽, 1~5 cctv 번호
# 총 k개의 cctv(5가지 종류)
    # 1(상/하/좌/우) , 2(상하/좌우) , 3(상좌/상우/좌하/우하)
    # 4(상좌우/상좌하/상우하/좌우하) , 5(상하좌우)
# 감시하는 방향의 칸 전체를 감시 가능 but 벽은 통과X
# cctv 회전 : 90도 방향 , 감시하려는 방향이 가로 or 세로
# 사무실의 크기와 상태, cctv 정보 => cctv 방향을 적절히 정해서 사각지대의 최소 크기

# 입력 : 사무실 세로 n, 가로 m (1~8)
# n개의 줄에 사무실 각 칸으 ㅣ정보
    # 0 빈칸 / 6 벽 / 1~5 cctv (8개 이하)
# 출력 : 사각지대의 최소 크기 출력

n,m = map(int,input().split())
graph = []
cctv = []
wall = 0
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if 1 <= graph[i][j] <= 5:
            cctv.append([graph[i][j],i,j])
        elif graph[i][j] == 6:
            wall += 1

maxSpot = -1
visited = [[False]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
direction = [[],[[0],[1],[2],[3]],[[0,1],[2,3]],[[0,2],[0,3],[1,2],[1,3]],[[0,1,3],[1,2,3],[0,1,2],[0,2,3]],[[0,1,2,3]]]

# 특정 방향의 보이는 spot개수 카운트 함수
def getSightedSpot(newChecked,x,y,dirList):
    spotNum = 0
    for dir in dirList:
        nx, ny = x, y
        while True:
            nx += dx[dir]
            ny += dy[dir]
            # 지도 밖이거나 벽이면 break
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 6:
                break
            # 빈칸인 경우 카운트하고 방문 표시
            if graph[nx][ny] == 0 and not newChecked[nx][ny]:
                spotNum += 1
                newChecked[nx][ny] = True
    return spotNum

def backtracking(idx,spot, checked):
    global maxSpot
    # 모든 cctv를 탐색했다면 return
    if idx == len(cctv):
        maxSpot = max(maxSpot,spot)
        return
    # cctv에서 보이는 spot을 탐색
    num,x,y = cctv[idx]
    for dirList in direction[num]:
        newChecked = [checked[i][:] for i in range(n)]
        backtracking(idx+1, spot + getSightedSpot(newChecked,x,y,dirList), newChecked)

backtracking(0,0,visited)

print(n*m - len(cctv) - wall - maxSpot)


# 4 6
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 1 0 6 0
# 0 0 0 0 0 0     # 20

# 6 6
# 0 0 0 0 0 0
# 0 2 0 0 0 0
# 0 0 0 0 6 0
# 0 6 0 0 2 0
# 0 0 0 0 0 0
# 0 0 0 0 0 5     # 15

# 6 6
# 1 0 0 0 0 0
# 0 1 0 0 0 0
# 0 0 1 0 0 0
# 0 0 0 1 0 0
# 0 0 0 0 1 0
# 0 0 0 0 0 1     # 6

# 6 6
# 1 0 0 0 0 0
# 0 1 0 0 0 0
# 0 0 1 5 0 0
# 0 0 5 1 0 0
# 0 0 0 0 1 0
# 0 0 0 0 0 1     # 2

# 1 7
# 0 1 2 3 4 5 6   # 0

# 3 7
# 4 0 0 0 0 0 0
# 0 0 0 2 0 0 0
# 0 0 0 0 0 0 4   # 0