# 연구소 (solving)
# 연구소 크기 n*m / 일부 칸 바이러스 존재, 벽은 칸 하나
# 바이러스 상하좌우 이동
# 새로 세울 수 있는 벽의 개수 3개
# 0: 빈칸 / 1: 벽 / 2: 바이러스
# 바이러스가 퍼질 수 없는 곳 : 안전영역
# 얻을 수 있는 안전 영역 크기의 최댓값

# 입력 : 세로 n , 가로 m (3<= n,m <= 8)
# n개의 줄에 지도의 모양

# 안전영역의 최대크기

# 문제 해결 방법
# (1) 벽을 세울 수 있는 3개 지점의 모든 조합 찾기(모든 경우의 수)
# (2) bfs 사용
    # 바이러스의 위치를 큐에 전부 넣고 while queue를 돌림
    # 바이러스를 퍼트린 후 0이 몇개 있는지 체크하고 최대값을 찾음
# (3) 최대값 출력

import sys
from collections import deque
from itertools import *

# 입력
n,m=map(int,sys.stdin.readline().split())
graph=[]
virus=[]
empty=[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    for j in range(m):
        if graph[i][j]==2:
            virus.append((i,j))
        if graph[i][j]==0:
            empty.append((i,j))
        
print(virus)

# bfs 함수
def bfs(graph,x,y):
    return

# main 코드
# 벽을 3개 세우는 케이스
empty=list(combinations(empty,3))





# 7 7
# 2 0 0 0 1 1 0                         # 2 1 0 0 1 1 2
# 0 0 1 0 1 2 0                         # 1 0 1 0 1 2 2
# 0 1 1 0 1 0 0                         # 0 1 1 0 1 2 2
# 0 1 0 0 0 0 0                         # 0 1 0 0 0 1 2
# 0 0 0 0 0 1 1                         # 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0                         # 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0       # 27              # 0 1 0 0 0 0 0

# 4 6
# 0 0 0 0 0 0                           # 0 0 0 0 1 2
# 1 0 0 0 0 2                           # 1 0 0 1 2 2 
# 1 1 1 0 0 2                           # 1 1 1 2 2 2
# 0 0 0 0 0 2         # 9               # 0 0 0 1 2 2

# 8 8
# 2 0 0 0 0 0 0 2                       # 2 2 2 2 2 2 2 2   
# 2 0 0 0 0 0 0 2                       # 2 2 2 2 2 2 2 2   
# 2 0 0 0 0 0 0 2                       # 2 2 2 2 2 2 2 2
# 2 0 0 0 0 0 0 2                       # 2 2 2 2 2 2 2 2
# 2 0 0 0 0 0 0 2                       # 2 2 2 2 2 2 2 2
# 0 0 0 0 0 0 0 0                       # 1 2 2 2 2 2 2 2
# 0 0 0 0 0 0 0 0                       # 0 1 2 2 2 2 2 2
# 0 0 0 0 0 0 0 0     # 3               # 0 0 1 2 2 2 2 2