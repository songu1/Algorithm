# 달이 차오른다, 가자. - bfs, 비트마스크 사용(풀이 참고)
# 직사각형 미로 탈출
    # 빈칸(.) : 이동가능
    # 벽(#) : 이동 불가능
    # 열쇠(a,b,c,d,e,f) : 이동 가능, 열쇠를 집음
    # 문(A,B,C,D,E,F) : 대응하는 열쇠가 있을 때만 이동 가능
    # 현재 위치(0) : 빈곳, 서있는곳
    # 출구(1) : 민식이가 가야하는 곳
# 한번의 움직임 : 상하좌우 1칸
# 민식이가 미로를 탈출하는데 걸리는 이동횟수의 최솟값을 구하는 프로그램

# 입력 : 미로의 세로크기 n, 가로크기 m (1~50)
# n개의 줄에 미로 모양이 주어짐
    # 같은 타입의 열쇠, 문 여러개 가능 / 대응하는 열쇠가 없을 수도 있음
    # 0은 1개, 1은 1개 이상
# 출력 : 미로를 탈출하는데 드는 이동 횟수의 최솟값 (불가능하면 -1)

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
maze = []
visited = [[[0]*7 for _ in range(m)] for _ in range(n)]     # 3차원 배열
for i in range(n):
    maze.append(list(map(str,sys.stdin.readline().rstrip())))
    for j in range(m):
        if maze[i][j] == '0':
            pos = (i,j)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs 함수
def bfs(graph,x,y):
    queue = deque([])
    visited[x][y][0] = 1
    graph[x][y] = '.'
    queue.append((x,y,0))
    print(*visited,sep="\n")
    print(key)
    while queue:
        x,y,k = queue.popleft()     # x,y:위치 / k : key별 평면
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == '#':
                continue
            # 빈칸 이동
            if graph[nx][ny] =='.' and not visited[nx][ny][k]:
                visited[nx][ny][k] = visited[x][y][k] + 1
                queue.append((nx,ny,k))
            # 문 이동
            elif 65 <= ord(graph[nx][ny]) <= 70:
                if key[k][ord(graph[nx][ny])-64]:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    queue.append((nx,ny,k))
            # 키 이동
            elif 97 <= ord(graph[nx][ny]) <= 102:
                nk = ord(graph[nx][ny])-96
                key[nk] = key[k][:]
                key[nk][nk] = True
                visited[nx][ny][nk] = visited[x][y][k] + 1
                graph[nx][ny] = '.'
                queue.append((nx,ny,nk))
            # 출구 이동
            elif graph[nx][ny] == '1':
                return visited[x][y][k]     # 출발지점의 이동횟수를 1로 설정했으므로 따로 -1 안해줌
            print(*visited,sep="\n")
            print(key)
    return -1

    
# main 코드
print(bfs(maze,pos[0],pos[1]))
print(*visited,sep="\n")
print(maze)

# 1 7
# f0.F..1             # 7

# 5 5
# ....1
# #1###
# .1.#0
# ....A
# .1.#.               # -1

# 7 8
# a#c#eF.1
# .#.#.#..
# .#B#D###
# 0....F.1
# C#E#A###
# .#.#.#..
# d#f#bF.1            # 55

# 3 4
# 1..0
# ###.
# 1...                # 3

# 3 5
# ..0..
# .###.
# ..1.A               # 6

# 4 5
# 0....
# .#B#A
# .#.#.
# b#a#1               # 19

# 1 11
# c.0.C.C.C.1         # 12

# 3 6
# ###...
# #0A.1a
# ###...              # -1

# 10 5
# #a##1
# #B##A
# .....
# ####.
# .....
# C####
# .....
# ##.#.
# ...#.
# c##b0               # 39

# 10 5
# #1##1
# #B##A
# .....
# ####.
# .....
# C####
# .....
# ##c#.
# ...#.
# a##b0               # 24

# 5 7
# f0aF...
# ###.#bA
# ###c##.
# #d#D##.
# 1..C..B             # 21