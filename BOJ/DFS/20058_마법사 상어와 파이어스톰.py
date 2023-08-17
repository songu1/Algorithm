# 마법사 상어와 파이어스톰 - dfs
# 크기 2^N * 2^N 격자 얼음판
# A[r][c] : (r,c)에 있는 얼음량(없으면 0)
# 파이어스톰 시전
    # 시전할 때마다 단계 L 결정
    # 격자를 2^L * 2^L의 부분 격자로 나눔
    # 모든 부분 격자를 시계방향으로 90회전
    # 얼음이 있는 칸 3개이상 인접해 있지 않은 칸은 얼음량 -1
# 상하좌우 인접
# 파이어스톰을 총 q번 시전
    # 모든 파이어스톰을 시전한 후 남아있는 얼음 A[r][c]의 합
    # 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
        # 덩어리 : 얼음 2칸 이상

# 입력 : n,q
# 2^n개의 줄에 각 칸에 있는 얼음량 배열 A
# 마법사 상어가 시전한 단계 L1,L2,...Lq
# 출력 : 남아있는 얼음의 합 A[r][c]의 합
# 가장 큰 덩어리가 차지하는 칸의 개수 (덩어리가 없으면 0 출력)

# 1차시도 : 45%에서 틀림 - 얼음 덩어리는 2개 이상이라는 것과 덩어리가 없으면 0 출력을 빼먹음
# 2차시도 : 성공~

# DFS
import sys
sys.setrecursionlimit(1000000)

n,q = map(int,sys.stdin.readline().split())
a=[]
for i in range(1,2**n+1):
    a.append(list(map(int,sys.stdin.readline().split())))
llist = list(map(int,sys.stdin.readline().split()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 격자 회전
def rotate(graph,n,l):
    new = [[0]*(2**n) for _ in range(2**n)]
    for i in range(0,2**n,2**l):
        for j in range(0,2**n,2**l):
            # 부분 격자 90도 회전
            for r in range(2**l):
                for c in range(2**l):
                    new[i+r][j+c] = graph[i+2**l-1-c][j+r]
    return new

# 인접 얼음 녹이기 함수
def iceMelting(graph):
    melt = []
    # 녹는 얼음 찾기
    for x in range(2**n):
        for y in range(2**n):
            if graph[x][y] > 0:     # 얼음이 있다면
                count = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx<0 or nx>=2**n or ny<0 or ny>=2**n or graph[nx][ny]==0:
                        continue
                    count += 1
                if count < 3:
                    melt.append((x,y))
    # 얼음 녹이기
    for (x,y) in melt:
        graph[x][y] -= 1
    return graph

# 가장 큰 얼음 덩어리 찾고 남아있는 얼음의 합 계산
def dfs(graph,x,y):
    global amount,size
    # 방문 처리
    amount += graph[x][y]
    size += 1
    graph[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=2**n or ny<0 or ny>=2**n:
            continue
        if graph[nx][ny] > 0:
            dfs(graph,nx,ny)
    return

for ll in llist:
    # 격자 회전
    a = rotate(a,n,ll)
    # print(*a,sep="\n")
    # print()
    # 얼음 녹이기
    a = iceMelting(a)
    # print(*a,sep="\n")
    # print()

amount = 0
largest = 0
for i in range(2**n):
    for j in range(2**n):
        # 남은 얼음의 양 계산 & 가장 큰 얼음 덩어리 찾기
        if a[i][j] > 0:   # 방문하지 않은 얼음만 dfs
            size = 0
            dfs(a,i,j)
            if size >= 2:
                largest = max(largest,size)
print(amount)
print(largest)

# 3 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1
# #
# 284
# 64

# 3 2
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2
# #
# 280
# 64

# 3 5
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 0 3 2
# #
# 268
# 64

# 3 10
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 0 3 2 1 2 3 2 3
# #
# 248
# 62

# 3 10
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# 1 2 3 1 2 3 1 2 3 1
# #
# 246
# 60

# 3 10
# 1 0 3 4 5 6 7 0
# 8 0 6 5 4 3 2 1
# 1 2 0 4 5 6 7 0
# 8 7 6 5 4 3 2 1
# 1 2 3 4 0 6 7 0
# 8 7 0 5 4 3 2 1
# 1 2 3 4 5 6 7 0
# 0 7 0 5 4 3 2 1
# 1 2 3 1 2 3 1 2 3 1
# #
# 37
# 9