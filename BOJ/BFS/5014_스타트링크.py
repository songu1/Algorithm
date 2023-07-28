# 스타트링크
# 총 F층으로 이루어진 고층 건물의 G층에 스타트링크가 있음
# 강호는 현재 S층 -> G층으로 이동하려함
# 버튼이 2개 있는 엘리베이터
    # U버튼 : 위로 U층을 가는 버튼
    # D버튼 : 아래로 D층을 가는 버튼
# 해당 층이 존재하지 않으면 움직이지 않음
# 강호가 G층에 도착하려면 버트을 적어도 몇번 눌러야하는지 구하는 프로그램
    # 이동할 수 없다면 "use the stairs"를 출력

# 입력 : f,s,g,u,d가 주어짐(1 <= s,g <= f <= 1000000 / u,d:0~1000000)
# 출력 : 강호가 S -> G로 가기위해 눌러야하는 버튼의 최솟값 출력 (이동불가시 use the stairs)

import sys
from collections import deque

f,s,g,u,d = map(int,sys.stdin.readline().split())
visited = [False]*(f+1)

dx=[u,-d]
# bfs 함수
def bfs(x):
    queue = deque([])
    visited[x] = True
    queue.append((0,x))
    while queue:
        count,x = queue.popleft()
        # G층에 도착한 경우
        if x == g:
            return count
        count += 1
        for i in range(2):
            nx = x + dx[i]
            if nx < 1 or nx > f:
                continue
            if not visited[nx]:
                visited[nx] = True
                queue.append((count,nx))
    return -1

# main 코드
count = bfs(s)
if count != -1:
    print(count)
else:
    print("use the stairs")

# 10 1 10 2 1     # 6

# 100 2 1 1 0     # use the stairs