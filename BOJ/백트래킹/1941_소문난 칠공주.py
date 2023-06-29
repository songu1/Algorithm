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
# 2차시도(힌트 봄) : 3%에서 틀림
    # 1. S가 4개 이상인 조합뽑기
    # 2. 뽑은 조합이 연달아 있는지 확인() - BFS
    # 3. 백트래킹


import sys
seat=[]
for i in range(5):
    seat = seat + list(map(str,sys.stdin.readline().rstrip()))
visited=[False]*25
resList=[]
case = 0
count = 0

# 조합으로 7개의 수 뽑기
idxList = []
def combinations(idx,arr,arrIdx):
    if arr.count("Y") >= 4:
        return
    if len(arr) == 7:
        idxList.append(arrIdx)
        # if arr.count("S")>=4:
        #     idxList.append(arrIdx)
        return
    for i in range(idx,25):
        combinations(i+1, arr + [seat[i]], arrIdx + [i])

combinations(0,[],[])

# dfs 함수
dx=[-5,5,-1,1]
def dfs(arr,x,visited):
    global count
    # 방문처리
    visited[x] = True
    count += 1
    if count == 7:
        return True
    # 주변 탐색
    for i in range(4):
        nx = x + dx[i]
        # print(nx)
        if nx <0 or nx>=25 or (i==2 and nx%5 == 4) or (i==3 and nx%5==0): # 상하좌우 값 X
            continue
        if not visited[nx] and nx in arr:
            if dfs(arr,nx,visited):
                return True
    return False
    
# main 함수
for ilist in idxList:
    if dfs(ilist,ilist[0],visited[:]):
        resList.append(ilist)
        case += 1
    count = 0

print(case)


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

# YYYYY
# SYSYS
# YYYYY
# YSYYS
# YYYYS 

# YYYYY
# YYYYS
# YYYYS
# YYYYS
# YYYYS

# YYYYY
# SYSYS
# YSYYY
# YYYYS
# YYYYY 

# SSSSS
# SSSSS
# SSSSS
# SSSSS
# SSSSY

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