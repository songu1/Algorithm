# 마법사 상어와 블리자드
# n*n 격자(n은 항상 홀수) / (1,1) => (n,n)
# 마법사 상어 위치 ( (n+1)/2, (n+1)/2 )
# 일부 칸과 칸 사이에는 벽이 세워져 있음 / 칸마다 번호
# 처음 상어 위치를 제외한 나머지칸 구술 하나(1,2,3번 구슬)
# 같은 번호를 가진 구슬이 연속하는 칸 => 연속하는 구슬
# 블리자드 마법 : 방향 di(상1 하2 좌3 우4), 거리 si 정함
    # (1) 상어는 di방향으로 거리가 si이하인 모든 칸에 구슬을 파괴(벽을 통과) => 빈칸 (벽은 그대로)
    # (2) a-1 빈칸이면, a칸의 구슬이 a-1칸으로 이동
        # 구슬이 더이상 이동하지 않을 때까지 반복 => 중간에 빈칸이 없음
    # (3) 4개 이상 연속하는 구슬이 있으면 폭발 (벽에 막히지 않은 경우)
    # (4) 다시 (2),(3) 반복
    # (5) 더 이상 폭발한 구슬이 없는 경우, 구슬 변화
        # 같은 번호 그룹(구슬 그룹) => a,b 2개로 변함
        # a : 그룹의 구슬 개수
        # b : 그룹을 이루는 구슬 번호
        # 구슬이 칸 수보다 많아 칸에 들어가지 못한다면 사라짐
# 블리자드를 총 m번 시전
# 마법의 정보 => 1*(폭발한 1번 구슬의 개수) + 2*(폭발한 2번 구슬의 개수) + 3*(폭발한 3번 구슬의 개수)

# 입력 : 격자 크기 n(3~49), 블리자드 횟수 m(1~100)
# n개의 줄 구슬의 정보 (구슬x, 상어 : 0)
# m개의 줄 블리자드 마법의 방향 di, 거리 si
# 출력 : 1*(폭발한 1번 구슬의 개수) + 2*(폭발한 2번 구슬의 개수) + 3*(폭발한 3번 구슬의 개수)

# 입력
n,m = map(int,input().split())
graph = [[0]*(n+1)]
for _ in range(n):
    graph.append([0] + list(map(int,input().split())))
shark = int((n+1)/2)
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

count = [0,0,0,0]       # 폭발한 구슬 개수(인덱스 1,2,3)


# 구슬 파괴 함수
def destroyMarble(graph,d,s):
    for i in range(1,s+1):
        nx = shark + dx[d]*i
        ny = shark + dy[d]*i
        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue
        graph[nx][ny] = 0


# 구슬 이동 : 그래프 => 리스트
def moveMarble(graph):
    arr = [0]
    dir = [3,2,4,1]
    x,y = shark, shark
    i,c,mc = 0,0,1
    while x != 0 and y != 0:
        x += dx[dir[i]]
        y += dy[dir[i]]
        # 구슬이 있다면 일차원 배열에 추가
        if graph[x][y] != 0:
            arr.append(graph[x][y])
        c += 1
        if c == mc:
            if i == 1 or i == 3:
                mc += 1
            c = 0
            i = (i+1)%4
    arr += [0]*(n*n-len(arr))
    return arr


# 구슬 폭발 함수
def exploreMarble(arr):
    c = 0
    compare = -1
    # 제일 뒤부터 폭발
    for i in range(len(arr)-1,-1,-1):
        # 구슬이 없는 경우
        if arr[i] == 0 and i != 0:
            continue
        # 이전 구슬과 같을 때
        if arr[i] == compare:
            c += 1
        # 이전 구슬과 다를 때
        else:
            # 이전 구슬그룹이 4개 이상일 때
            if c >= 4:
                count[compare] += c
                for j in range(c,0,-1):
                    del arr[i+j]
            # 다시 구슬 그룹 카운트
            c = 1
            compare = arr[i]
    remove = n*n - len(arr)
    arr += [0]*remove
    return remove


# 구슬 변화 함수 : 리스트 => 그래프
def changeMarble(graph, arr):
    graph = [[0]*(n+1) for _ in range(n+1)]
    marble = [0,0]      #(개수, 구슬번호)
    dir = [3,2,4,1]
    x,y = shark, shark
    k, c, mc = 0, 0, 1
    for i in range(1,len(arr)):
        if arr[i] == marble[1]:
            marble[0] += 1
        else:
            # 그래프에 추가
            if marble != [0,0]:     # 제일 처음 
                for j in range(2):
                    x += dx[dir[k]]
                    y += dy[dir[k]]
                    graph[x][y] = marble[j]
                    c += 1
                    if c == mc:
                        if k == 1 or k == 3:
                            mc += 1
                        c = 0
                        k = (k+1)%4

            # 다음 그룹 카운트
            marble[0] = 1
            marble[1] = arr[i]

        # # 구슬이 칸보다 많은 경우
        if x == 1 and y == 1:
            break
    return graph

# main 코드
for _ in range(m):
    d,s = map(int,input().split())
    destroyMarble(graph,d,s)    # 구슬 파괴
    arr = moveMarble(graph)     # 구슬 이동
    while True:                 # 구슬 폭발
        if exploreMarble(arr) == 0:
            break
    graph = changeMarble(graph,arr) # 구슬 변화

print(count[1]*1 + count[2]*2 + count[3]*3)

# 7 1
# 0 0 0 0 0 0 0
# 3 2 1 3 2 3 0
# 2 1 2 1 2 1 0
# 2 1 1 0 2 1 1
# 3 3 2 3 2 1 2
# 3 3 3 1 3 3 2
# 2 3 2 2 3 2 3
# 2 2                     # 28

# 7 4
# 0 0 0 2 3 2 3
# 1 2 3 1 2 3 1
# 2 3 1 2 3 1 2
# 1 2 3 0 2 3 1
# 2 3 1 2 3 1 2
# 3 1 2 3 1 2 3
# 1 2 3 1 2 3 1
# 1 3
# 2 2
# 3 1
# 4 3                     # 0

# 7 4
# 1 1 1 2 2 2 3
# 1 2 2 1 2 2 3
# 1 3 3 2 3 1 2
# 1 2 2 0 3 2 2
# 3 1 2 2 3 2 2
# 3 1 2 1 1 2 1
# 3 1 2 2 2 1 1
# 1 3
# 2 2
# 3 1
# 4 3                     # 39

# 7 7
# 1 1 1 2 2 2 3
# 1 2 2 1 2 2 3
# 1 3 3 2 3 1 2
# 1 2 2 0 3 2 2
# 3 1 2 2 3 2 2
# 3 1 2 1 1 2 1
# 3 1 2 2 2 1 1
# 1 3
# 2 2
# 3 1
# 4 3
# 1 3
# 1 1
# 1 3                     # 62