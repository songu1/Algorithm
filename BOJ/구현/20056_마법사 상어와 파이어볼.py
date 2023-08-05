# 마법사 상어와 파이어볼 - 블로그 꼭 적어야함
# https://jennnn.tistory.com/77 참고
# N*N 격자에 파이어볼 M개 - 위치 (ri, ci) / 질량 mi / 방향 di / 속력 si
# 격자의 행과 열 1~n번 번호 (1번행-n번행 / 1번열-n번열 연결)
# 파이어볼 방향 : 인접한 8개의 칸의 방향(상부터 시계방향으로 0~7)
# 파이어볼 이동 규칙
    # 1) 자신의 방향 di로 si칸 만큼 이동 (같은 칸에 여러개의 파이어볼이 있을 수 있음)
    # 2) 이동이 끝난 후 ,2개 이상의 파이어볼이 있는 경우
        # a) 같은 칸의 파이어볼은 모두 하나로 합쳐짐
        # b) 파이어볼은 4개의 파이어볼로 나누어짐
        # c) 나누어진 파이어볼
            # 질량 : ⌊(합쳐진 파이어볼 질량의 합)/5⌋                            : 바닥함수(버림)
            # 속력 :  ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋        : 바닥함수(버림)
            # 합쳐지는 파이어볼 방향이 모두 홀수 or 짝수 -> 방향 0,2,4,6
            # 아니면 -> 방향 1,3,5,7
        # d) 질량이 0인 파이어볼은 소멸되어 사라짐
# 마법사 상어가 이동을 k번 명령한 수 남아있는 파이어볼 질량의 합

# ⌊ 바닥함수(버림), 천장함수(올림) 구분하기

# 입력 : n(4~50),m(0~n^2),k (1~1000)
# m개의 파이어볼 정보 r,c,m,s,d
# 마법사 상어가 이동을 k번 명령한 후 남아있는 파이어볼 질량의 합

# 1차시도 : 시간초과 - sort() 때문에 난듯?
# 2차시도 : set에서 시간초과가 난 듯
# 3차시도 : 통과 - 질량이 0인 파이어볼 소멸하는 코드가 없어 시간 초과가 남 + 3차원 배열로 구현

import sys

n,m,k = map(int,sys.stdin.readline().split())
fireball = []
for i in range(m):
    fireball.append(list(map(int,sys.stdin.readline().split())))
graph = [[[] for _ in range(n+1)] for _ in range(n+1)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

# 파이어볼 이동 함수
def moveFireball(fireball):
    # graph = [[[] for _ in range(n+1)] for _ in range(n+1)]
    # 모든 파이어볼을 이동 후 정보 저장
    for i in range(len(fireball)):
        nx = fireball[i][0] + dx[fireball[i][4]]*fireball[i][3]
        ny = fireball[i][1] + dy[fireball[i][4]]*fireball[i][3]
        if nx<1 or nx >n or ny<1 or ny>n:
            nx %= n
            ny %= n
            if nx == 0: nx = n
            if ny == 0: ny = n
        graph[nx][ny].append([fireball[i][2], fireball[i][3], fireball[i][4]])  # m, s, d 저장
    # print(*graph,sep="\n")
    # print(index)
    # 각 위치의 파이어볼 선택
    moved = []
    for x in range(1,n+1):
        for y in range(1,n+1):
            # 파이어볼이 1개 있을 때
            if len(graph[x][y]) == 1:
                moved.append([x,y]+graph[x][y].pop())
            # 파이어볼이 여러개 있을 때
            elif len(graph[x][y]) > 1:
                c = len(graph[x][y])
                fm, fs, even, odd = 0, 0, 0, 0
                while graph[x][y]:
                    fb = graph[x][y].pop()
                # for fb in graph[x][y]:
                    fm += fb[0]
                    fs += fb[1]
                    if fb[2]%2:
                        odd += 1
                    else:
                        even += 1
                fm //= 5                # 파이어볼 질량
                fs //= c                # 파이어볼 속력
                # 파이어볼 방향
                if odd == 0 or even == 0:
                    dir = [0,2,4,6]
                else:
                    dir = [1,3,5,7]
                if fm != 0:
                    for i in range(4):
                        moved.append([x,y,fm,fs,dir[i]])
    return moved

# main 코드
for _ in range(k):
    fireball = moveFireball(fireball)

result = 0
for fb in fireball:
    result += fb[2]
print(result)

# 4 2 1
# 1 1 5 2 2
# 1 4 7 1 6           # 8

# 4 2 2
# 1 1 5 2 2
# 1 4 7 1 6           # 8

# 4 2 3
# 1 1 5 2 2
# 1 4 7 1 6           # 0

# 7 5 3
# 1 3 5 2 4
# 2 3 5 2 6
# 5 2 9 1 7
# 6 2 1 3 5
# 4 4 2 4 2           # 9

# 1차 시도 - 시간초과
# import sys

# n,m,k = map(int,sys.stdin.readline().split())
# fireball = []
# for i in range(m):
#     fireball.append(list(map(int,sys.stdin.readline().split())))

# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1]
# def moveFireball(fireball):
#     visited = [[0]*(n+1) for _ in range(n+1)]
#     # 모든 파이어볼을 이동 후 정보 저장
#     for i in range(len(fireball)):
#         nx = fireball[i][0] + dx[fireball[i][4]]*fireball[i][3]
#         ny = fireball[i][1] + dy[fireball[i][4]]*fireball[i][3]
#         if nx<1 or nx >n or ny<1 or ny>n:
#             nx %= n
#             ny %= n
#             if nx == 0: nx = n
#             if ny == 0: ny = n
#         fireball[i][0] = nx
#         fireball[i][1] = ny
#         visited[nx][ny] += 1
#     fireball.sort(key=lambda x:(x[0],x[1]))
#     # print("이동",fireball)
#     # 각 위치의 파이어볼 선택
#     i = 0
#     moved = []
#     while i < len(fireball):   # 0:r / 1:c / 2:m / 3:s / 4:d
#         if visited[fireball[i][0]][fireball[i][1]] <= 1:
#             moved.append(fireball[i])
#             i += 1
#             continue
#         c = visited[fireball[i][0]][fireball[i][1]]     # 파이어볼 개수
#         fm, fs = 0, 0
#         fd = []
#         for j in range(i,i+c):
#             fm += fireball[j][2]
#             fs += fireball[j][3]
#             fd.append(fireball[j][4]%2)
#         fm //= 5                # 파이어볼 질량
#         fs //= c                # 파이어볼 속력
#         # 파이어볼 방향
#         if 0 < fd.count(0) < c:
#             dir = [1,3,5,7]
#         else:
#             dir = [0,2,4,6]
#         for j in range(4):
#             moved.append([fireball[i][0],fireball[i][1],fm,fs,dir[j]])
#         # 다음 위치
#         i += c
#     # print("완료",moved)
#     return moved

# # main 코드
# for i in range(k):
#     fireball = moveFireball(fireball)

# result = 0
# for fb in fireball:
#     result += fb[2]
# print(result)

# 2차시도 - 시간 초과 : set 사용
# 각 위치의 파이어볼 선택 부분
    # moved = []
    # for (x,y) in index:
    #     # 파이어볼이 1개 있을 때
    #     if len(graph[x][y]) == 1:
    #         moved.append([x,y]+graph[x][y][0])
    #         continue
    #     # 파이어볼이 여러개 있을 때
    #     c = len(graph[x][y])
    #     fm, fs, fd = 0, 0, []
    #     for fb in graph[x][y]:
    #         fm += fb[0]
    #         fs += fb[1]
    #         fd.append(fb[2]%2)
    #     fm //= 5                # 파이어볼 질량
    #     fs //= c                # 파이어볼 속력
    #     # 파이어볼 방향
    #     if 0 < fd.count(0) < c:
    #         dir = [1,3,5,7]
    #     else:
    #         dir = [0,2,4,6]
    #     for i in range(4):
    #         moved.append([x,y,fm,fs,dir[i]])