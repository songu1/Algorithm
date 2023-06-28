# 소문난 칠공주
# 25명의 여학생 - 5*5 형태로 배치 (이다솜파, 임도연파)
# 임도연파 > 이다솜파 -> 이다솜파 체제 포기, 소문난 칠공주 결성
# 규칙
    # 7명의 여학생으로 구성
    # 7명의 자리는 서로 가로,세로로 인접해야함
    # 파 상관 X but 이다솜파 >= 4
# 자리 배치도 -> 소문난 칠공주를 결성할 수 있는 모든 경우의 수

# 입력 : S(이다솜파), Y(임도연파)를 값으로 갖는 5*5 행렬(공백X)
    # S가 4명 이상
# 출력 : 소문난 칠공주를 결성할 수 있는 모든 경우의 수

# dfs인데 방향을 두 방향으로만..?

# 1차시도 : 11%에서 틀림
# 2차시도(힌트 봄) : 
    # 1. S가 4개 이상인 조합뽑기
    # 2. 뽑은 조합이 연달아 있는지 확인() - BFS
    # 3. 백트래킹


import sys
seat=[]
graph=[]
for i in range(5):
    seat.append(list(map(str,sys.stdin.readline().rstrip())))
    for j in range(5):
        graph.append(seat[i][j])
print(graph)
visited=[[False]*5 for _ in range(5)]
resList=[]
case = 0

# 조합으로 7개의 수 뽑기
idxList=[]
def combinations(idx,arr,arrIdx):
    if arr.count("Y") >= 4:
        return
    if len(arr) == 7:
        if arr.count("S")>=4:
            idxList.append(arrIdx)
        return
    for i in range(idx,25):
        combinations(i+1, arr + [graph[i]], arrIdx + [i])

for i in range(25):
    combinations(0,[],[])
print(idxList)
print(len(idxList))
    

# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
# def backtracking(arr,x,y,pre):
#     global case
#     if arr.count("Y") >= 4:
#         return
#     if len(arr) == 7:
#         res = pre[:]
#         res.sort()
#         if res not in resList:
#             case += 1
#             resList.append(res)
#             print(res)
#             # print(arr)
#             print(resList)
#             print()
#         return
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx<0 or ny<0 or nx>=5 or ny>=5:
#             continue
#         if not visited[nx][ny]:
#             visited[nx][ny] = True
#             pre.append((nx,ny))
#             backtracking(arr + [seat[nx][ny]],nx, ny,pre)
#             visited[nx][ny] = False
#             pre.pop()
    
# for i in range(5):
#     for j in range(5):
#         visited[i][j] = True
#         backtracking([seat[i][j]],i,j,[(i,j)])
#         visited = [[False]*5 for _ in range(5)]

# print(case)
# print(len(resList))

# YYYYY
# SYSYS
# YYYYY
# YSYYS
# YYYYY       # 2

# SYSYY
# YYYYY
# YYSYY
# YYYYY
# YYSYY       # 1

# 힌트
# .....    .....
# SYSYS    SYSYS
# ....Y    .Y...
# ....S    .S...
# .....    .....

# .....
# SYS..
# ..YY.
# .SY..
# ..... 