# 점프 점프 - 7분 + 
# 각 칸에 정수가 쓰여 있는 1*n 미로에 갇혀있음
# i번째 칸에 쓰인 수를 Ai라고 했을 때 Ai이하만큼 오른쪽으로 떨어진 칸에 한번에 점프 가능
    # i=3, A3=3 -> 4(3+1), 5(3+2), 6(3+3)으로 점프 가능
# 미로의 왼쪽 끝 -> 오른쪽 끝으로 갈 때 최소 몇번 점프해야 갈 수 있는지
    # 없다면 -1출력

# 입력 : n(1~1000)
# Ai값이 주어짐 (0~100)
# 출력 : 재환이가 최소 몇 번 점프를 해야 가장 오른쪽 끝칸으로 갈 수 있는지 (없다면 -1)

# BFS를 사용하는 이유 : 점프횟수를 효율적으로 구하기위해서 (점프횟수 순서대로 QUEUE에서 꺼냄)
    # 방문을 하기만 하면 무조건 최소 방문 횟수가 됨

import sys
from collections import deque
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
a.insert(0,-1)

d=[-1]*(n+1)   # 점프 횟수 배열

# bfs 함수(dp포함)
def bfs(graph,d):
    queue=deque([])
    # 임의로 인덱스 0 처리(실제 사용X)
    # d[0]=-1 
    queue.append((0,1))    # 현재 위치, 점프할 수 있는 위치
    while queue:
        x,y=queue.popleft()
        if d[y] == -1:   # 방문하지 않았다면
            # 점프할 수 있는 위치로 점프
            d[y]=d[x]+1 # 점프 횟수 계산
            # 점프한 위치에서 점프할 수 있는 위치
            for i in range(1,graph[y]+1):
                if y+i <= n:
                    queue.append((y,y+i))    # 점프한 위치, 점프한 위치에서 점프할 수 있는 위치
    return d[n]

# main함수
print(bfs(a,d))





# 10
# 1 2 0 1 3 2 1 5 4 2     # 5
