# 양
# 마당 - .:빈 필드 / #:울타리 / o:양 / v:늑대
# 상하좌우 이동가능 -> 같은 영역안
# 마당에서 탈출가능한 칸은 어떤 영역에도 속하지 않음
# 영역안의 양의수 > 늑대수 : 늑대 쫒아냄
# 양의수 <= 늑대수 : 양 잡아먹힘
# 아침이 도달했을 때 살아남은 양과 늑대의 수를 출력하는 프로그램

# 입력 : r,c (1~250)
# 마당의 구조
# 출력 : 아침까지 살아있는 양과 늑대의 수

import sys
from collections import deque

r,c = map(int,sys.stdin.readline().split())
field = []
for _ in range(r):
    field.append(list(map(str,sys.stdin.readline().rstrip())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs 함수
def bfs(field,x,y):
    queue = deque([])
    s = 0
    w = 0
    # 방문 처리
    if field[x][y] == "o":
        s += 1
    elif field[x][y] == "v":
        w += 1
    field[x][y] = "*"   # 방문 처리
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=r or ny<0 or ny>=c or field[nx][ny]=="#":
                continue
            if field[nx][ny] != "*":    # 이미 방문하지 않은 경우
                # 양
                if field[nx][ny] == "o":
                    s += 1
                # 늑대
                elif field[nx][ny] == "v":
                    w += 1
                field[nx][ny] = "*"
                queue.append((nx,ny))
    if s>w:
        return s,0
    return 0,w

sheep, wolf = 0,0
for i in range(r):
    for j in range(c):
        if field[i][j]!="#" or field[i][j]!="*":
            s,w = bfs(field,i,j)
            sheep += s
            wolf += w
print(sheep, wolf)

# 6 6
# ...#..
# .##v#.
# #v.#.#
# #.o#.#
# .###.#
# ...###          # 0 2

# 8 8
# .######.
# #..o...#
# #.####.#
# #.#v.#.#
# #.#.o#o#
# #o.##..#
# #.v..v.#
# .######.        # 3 1

# 9 12
# .###.#####..
# #.oo#...#v#.
# #..o#.#.#.#.
# #..##o#...#.
# #.#v#o###.#.
# #..#v#....#.
# #...v#v####.
# .####.#vv.o#
# .......####.    # 3 5