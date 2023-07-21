# 맥주 마시면서 걸어가기
# 상근이네 집에서 출발
# 맥주 한박스(20병)
    # 50미터에 한병씩 마심(맥주 한병을 마셔야 갈 수 있음)
# 맥주 구매 : 빈병을 버리고 새 맥주병을 살 수 있음 (최대 20병만 들고갈 수 있음)
# 편의점, 상근이네집, 펜타포트 락 페스티벌 좌표 -> 행복하게 페스티벌에 도착할 수 있는지

# 입력 : 테스트케이스 수 t(1~50)
# 맥주를 파는 편의점 수 n (0~100)
# n+2개의 줄에 상근이네집, 편의점 ,펜타의 x,y 좌표 (-32768 ~ 32767)
    # 두 좌표사이의 거리 = x좌표 차이 + y좌표 차이 => 상하좌우 이동
# 출력 : 각 테스트케이스에 대해서 행복하게 페스티벌에 가면 happy 아니면 sad를 출력

# 1차 시도 : 런타임에러 (value error)- queue에서 뺀 값을 stores.remove을 실행 -> queue에 같은 값이 여러개 있는 경우 컴파일 에러

# 2차시도 : 통과 (탐색할 때 stores 배열에서 빼기 + stores의 마지막 원소부터 제거)

# 3차 시도 : 통과 (주변 탐색할때 stores배열을 확인하는 것이 아니라 visited배열로 방문 여부 확인해주기)

# 3차 시도
import sys
from collections import deque

# bfs 함수
def bfs(stores,start,end,visited):
    queue = deque([])
    queue.append((start[0],start[1]))
    while queue:
        x,y = queue.popleft()
        # 펜타포트에 도착 가능한지 체크
        if abs(x-end[0]) + abs(y-end[1]) <= 1000:
            return "happy"
        # 편의점 방문
        for i in range(n):
            if not visited[i] and abs(stores[i][0]-x) + abs(stores[i][1]-y) <= 1000:
                queue.append((stores[i][0],stores[i][1]))
                visited[i] = True
        
    return "sad"

t = int(sys.stdin.readline())
for _ in range(t):
    # 입력
    n = int(sys.stdin.readline())
    visited = [False]*n
    start = list(map(int,sys.stdin.readline().split()))
    stores = []
    for _ in range(n):
        stores.append(list(map(int,sys.stdin.readline().split())))
    finish = list(map(int,sys.stdin.readline().split()))
    
    #  main 코드
    print(bfs(stores,start,finish,visited))


# 2차 시도
# import sys
# from collections import deque

# # bfs 함수
# def bfs(stores,x,y,ex,ey):
#     queue = deque([])
#     queue.append((x,y))
#     while queue:
#         x,y = queue.popleft()
#         # 펜타포트에 도착 가능한지 체크
#         if abs(x-ex) + abs(y-ey) <= 1000:
#             return "happy"
#         # 편의점 방문
#         for i in range(len(stores)-1,-1,-1):
#             if abs(stores[i][0]-x) + abs(stores[i][1]-y) <= 1000:
#                 queue.append((stores[i][0],stores[i][1]))
#                 stores.remove(stores[i])
        
#     return "sad"

# t = int(sys.stdin.readline())
# for _ in range(t):
#     # 입력
#     n = int(sys.stdin.readline())
#     stores = []
#     for _ in range(n+1):
#         stores.append(list(map(int,sys.stdin.readline().split())))
#     finish = list(map(int,sys.stdin.readline().split()))
    
#     #  main 코드
#     print(bfs(stores,stores[0][0],stores[0][1],finish[0],finish[1]))

# 2
# 2
# 0 0
# 1000 0
# 1000 1000
# 2000 1000
# 2
# 0 0
# 1000 0
# 2000 1000
# 2000 2000
# #
# happy
# sad

# 1
# 5
# 0 0
# 900 0
# 2000 1000
# 0 1000
# 0 2000
# 1000 2000
# 2000 2000
# # 
# happy

