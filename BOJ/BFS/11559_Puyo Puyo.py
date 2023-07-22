# Puyo Puyo
# 필드에 여러 색의 뿌요
# 1) 아래에 바닥이나 다른 뿌요가 나올 때 까지 아래로 떨어짐)
# 2) 같은색 뿌요가 4개 이상 상하좌우 연결 -> 같은 색의 뿌요들이 한꺼번에 없어짐
# 1,2번 계속 반복
# 터질 수 있는 뿌요 여러그룹 -> 동시에 터져야함
# 상대방의 필드 -> 연쇄가 몇번 연속으로 일어날지 계산하는 프로그램

# 입력 : 12개줄에 필드의 정보(각 줄에 6개 문자)
    # . : 빈공간 / R : 빨 / G : 초 / B : 파 / P : 보 / Y : 노
    # 입력은 뿌요들이 모두 아래로 떨어진 뒤(뿌요 아래 빈칸x)
# 출력 : 현재 주어진 상황에서 몇 연쇄가 되는지 출력 (안터지면 0 출력)

import sys
from collections import deque

field = []
for i in range(12):
    field.append(list(map(str,sys.stdin.readline().rstrip())))

# bfs 함수
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(field,x,y):
    color = field[x][y]
    queue = deque([])
    arr = [(x,y)]
    visited[x][y] = True
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=12 or ny<0 or ny>=6:
                continue
            if not visited[nx][ny] and field[nx][ny] == color:
                arr.append((nx,ny))
                visited[nx][ny] = True
                queue.append((nx,ny))
    if len(arr) >= 4:
        return arr
    return []

result = 0
while True:
    res = []
    visited = [[False]*6 for _ in range(12)]
    # bfs로 4개 이상 연결된 뿌요 찾기
    for i in range(12):
        for j in range(6):
            if field[i][j]!= '.' and not visited[i][j]:
                res += bfs(field,i,j)
    # 연쇄된 뿌요가 없다면
    if len(res) == 0:
        break
    # 뿌요 연쇄 및 떨어뜨리기
    result += 1
    for r in res:
        if r[0]>=1:
            for k in range(r[0],0,-1):
                field[k][r[1]] = field[k-1][r[1]]
                field[k-1][r[1]] = '.'

print(result)

# ......
# ......
# ......
# ......
# ......
# ......
# ......
# ......
# .Y....
# .YG...
# RRYG..
# RRYGG.      # 3
