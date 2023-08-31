# 녹색 옷 입은애가 젤다지?
# 도둑루피 -> 소지한 루피 감소
# 도둑루피만 가득한 n*n 크기 동굴
# (0,0) -> (n-1,n-1)칸까지 이동해야함 (상하좌우 이동)
# 각 칸을 지날 때 해당 도둑루피 크기만큼 소지금 잃음
# 잃는 금액을 최소로하여 동굴 건너편까지 이동

# 입력 : (여러개의 테스트케이스)
# 동굴의 크기 n(2~125) (n=0이면 입력 종료)
# n개의 줄에 각 칸의 도둑루피 크기 k(0~9)
# 출력 : 각 테스트케이스마다 잃는 금액을 한줄에 걸쳐 정답을 형식에 맞춰 출력 - 최소합으로

import sys
import heapq

INF = int(1e9)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dijkstra(x,y):
    q = []
    heapq.heappush(q,(graph[x][y],x,y))
    distance[x][y] = graph[x][y]
    while q:
        rupee, x, y = heapq.heappop(q)
        if distance[x][y] < rupee:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            cost = rupee + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q,(cost,nx,ny))

i = 0
while True:
    i += 1
    n = int(sys.stdin.readline())
    if n == 0:
        break
    distance = [[INF]*n for _ in range(n)]
    graph = []
    for _ in range(n):
        graph.append(list(map(int,sys.stdin.readline().split())))
    dijkstra(0,0)
    print("Problem "+str(i)+": "+str(distance[n-1][n-1]))

# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
# 0
# #
# Problem 1: 20
# Problem 2: 19
# Problem 3: 36