# 로봇 청소기
# 초봇 청소기와 방의 상태 -> 청소하는 영역의 개수 구하기
# 방 : n*m / 칸은 벽 또는 빈칸(r,c) : (0,0) ~ (n-1,m-1)
# 청소가 동서남북을 바라봄
# 작동 방식
    # 현재 칸 청소되지 않음 -> 청소
    # 현재 칸 주변 4칸 중 청소되지 않은 빈칸 없음
        # 바라보는 방향 유지, 한칸 후진 가능 -> 한칸 후진 후 1번
        # 바라보는 방향 뒷칸이 벽 -> 작동을 멈춤
    # 현재 칸 주변 4칸 중 청소되지 않은 빈칸 있음
        # 반시계방향으로 90도 회전 (북 - 서 - 남 - 동) : 현재방향의 다음 방향부터
        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈칸인 경우 전진
        # 1번으로 돌아감

# 입력 : 방 크기 n,m (3~50)
# 처음 로봇 청소기가 있는 칸의 좌표(r,c) / 방향 d(0:북 / 1:동 / 2:남 / 3:서)
# n개의 줄에 각 장소의 상태 (0:청소X / 1:벽)
# 출력 : 로봇 청소기가 작동을 시작한 후 멈출 때까지 청소하는 칸의 개수

# 반복문으로 풀어보기!!


import sys
# 입력
n,m = map(int, sys.stdin.readline().split())
r,c,d = map(int, sys.stdin.readline().split())
graph=[]        # 0:청소X / 1:벽 / 2:청소O
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

# 북,동,남,서
dx=[-1,0,1,0]
dy=[0,1,0,-1]
index=[3,0,1,2]
x=r
y=c
c=1
while True:
    find=False
    # 현재 칸 청소
    graph[x][y]=2
    # 주변 4칸 탐색
    i=d
    for _ in range(4):
        # 방향계산
        i=index[i]
        # 이동
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        # 청소되지 않은 칸 탐색
        if graph[nx][ny]==0:
            x=nx
            y=ny
            d=i
            find=True
            c+=1
            break
    # 모두 다 회전했을 때
    if find==False:
        if i<=1:
            nx=x+dx[i+2]
            ny=y+dy[i+2]
        else:
            nx=x+dx[i-2]
            ny=y+dy[i-2]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if graph[nx][ny]==1:
                break
            x=nx
            y=ny
            d=i
                    
print(c)

# main
# count=0
# print("그래프")
# for i in range(n):
#     for j in range(m):
#         print(graph[i][j],end=' ')
#         if graph[i][j]==2:
#             count+=1
#     print("")
# print(count)






# 3 3
# 1 1 0
# 1 1 1
# 1 0 1
# 1 1 1                   #1

# 11 10
# 7 4 0
# 1 1 1 1 1 1 1 1 1 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 1 1 1 1 0 1
# 1 0 0 1 1 0 0 0 0 1
# 1 0 1 1 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 1 0 1
# 1 0 0 0 0 0 1 1 0 1
# 1 0 0 0 0 0 1 1 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1     # 57