# 마법사 상어와 비바라기
# n*n 격자에 칸마다 바구니가 있음-물을 무한으로 저장 가능
# 1번행, n번행 연결 / 1번열,n번열 연결
# 비바라기
    # (1) (n,1) (n,2) (n-1,1) (n-1,2)에 비구름이 생김
        # => (n-1,0) (n-1,1) (n-2,0) (n-2,1)
    # (2) 이동 m번 명령 (8개의 방향 di, 거리 si) 좌 좌상 상 상우 우 우하 하 하좌
# 이동 순서
    # (1) 모든 구름이 di방향으로 si칸 이동
    # (2) 각 구름에서 비가 내려 바구니에 저장된 물 1 증가
    # (3) 구름이 모두 사라짐
    # (4) (2)에서 물이 증가한칸 -> 대각선 1칸 옆에 물이있는 바구니의 수만큼 바구니 물 증가
        # 경계는 해당X
    # (5) 바구니에 저장된 물의 양이 2이상 => 구름 생기고 물의양 -2 (구름이 사라진칸X)
# m번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합

# 입력 : n(2~50),m(1~100)
# n개의 줄에 n개의 정수 : 바구니에 저장되어있는 물의 양
# m개의 줄에 이동의 정보 di,si
# 출력 : m번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합

# 1차시도 : 1%에서 시간초과

import sys

n,m = map(int,sys.stdin.readline().split())
basket = []
move =[]
visited = [[False]*n for _ in range(n)]
for _ in range(n):
    basket.append(list(map(int,sys.stdin.readline().split())))
for _ in range(m):
    move.append(list(map(int,sys.stdin.readline().split())))

dx = [9,0,-1,-1,-1,0,1,1,1]       # 2,4,6,8 : 대각선
dy = [9,-1,-1,0,1,1,1,0,-1]

# 구름이동 및 비내리기 함수
def rain(basket,cloud,d,s,visited):
    for i in range(len(cloud)):
        x,y = cloud[i]
        nx = (x + s*dx[d]) % n
        ny = (y + s*dy[d]) % n
        cloud[i] = (nx,ny)
        basket[nx][ny] += 1
        visited[nx][ny] = True

# 물복사버그 함수 & visited배열에 구름 유무 저장
def waterBug(basket, cloud):
    while cloud:
        x,y = cloud.pop()
        count = 0
        for j in range(2,10,2):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if basket[nx][ny] != 0:
                count += 1
        basket[x][y] += count

# 새로운 구름 생성 함수
def createCloud(basket,cloud,visited):
    for i in range(n):
        for j in range(n):
            if basket[i][j] >=2 and not visited[i][j]:
                cloud.append((i,j))
                basket[i][j] -= 2
            elif visited[i][j]:
                visited[i][j] = False

    
cloud = [(n-1,0), (n-1,1), (n-2,0), (n-2,1)]
for i in range(m):
    # 구름 이동 및 비내리기
    d,s = move[i]
    rain(basket,cloud,move[i][0],move[i][1],visited)
    # 물복사버그
    waterBug(basket, cloud)
    # backet이 2이상인 곳 구름 생성(이전 클라우드 제외)
    createCloud(basket,cloud,visited)

# 바구니 물의 합
res = 0
for i in range(n):
    res += sum(basket[i])
print(res)


# 5 4
# 0 0 1 0 2
# 2 3 2 1 0
# 4 3 2 9 0
# 1 0 2 9 0
# 8 8 2 1 0
# 1 3
# 3 4
# 8 1
# 4 8                     # 77

# 5 8
# 0 0 1 0 2
# 2 3 2 1 0
# 0 0 2 0 0
# 1 0 2 0 0
# 0 0 2 1 0
# 1 9
# 2 8
# 3 7
# 4 6
# 5 5
# 6 4
# 7 3
# 8 2                     # 41

# 5 8
# 100 100 100 100 100
# 100 100 100 100 100
# 100 100 100 100 100
# 100 100 100 100 100
# 100 100 100 100 100
# 8 1
# 7 1
# 6 1
# 5 1
# 4 1
# 3 1
# 2 1
# 1 1                         # 2657