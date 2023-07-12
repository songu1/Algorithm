# 헌내기는 친구가 필요해
# 대학 캠퍼스 n*m 크기
# 벽이 아닌 상하좌우 이동, 캠퍼스 밖으로 이동 불가
# 캠퍼스에서 도연이가 만날 수 있는 사람의 수 출력

# 입력 : 캠퍼스의 크기 n,m(1~600)
# 캠퍼스 정보 (o:빈공간 / x:벽 / I:도연 / P:사람)
# 출력 : 도연이가 만날 수 있는 사람의 수(아무도 못만날 경우 TT 출력)

import sys
sys.setrecursionlimit(1000000)

n,m = map(int,sys.stdin.readline().split())
campus = []
visited = [[False]*m for _ in range(n)]
num = 0
for i in range(n):
    campus.append(list(map(str,sys.stdin.readline().rstrip())))
    for j in range(m):
        if campus[i][j] == 'I':
            posX=i
            posY=j

# dfs 함수 ver1 (시간 큼)
def dfs(campus,x,y,visited):
    global num
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if campus[x][y]!= 'X' and not visited[x][y]:
        # 방문처리
        visited[x][y] = True
        # 사람 만남
        if campus[x][y] == 'P':
            num += 1
        # 주변 탐색
        dfs(campus,x-1,y,visited)
        dfs(campus,x+1,y,visited)
        dfs(campus,x,y-1,visited)
        dfs(campus,x,y+1,visited)
        return True
    return False

# dfs 함수 ver2 (메모리 큼)
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# def dfs(campus,x,y,visited):
#     global num
#     # 방문처리
#     visited[x][y] = True
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx<0 or nx>=n or ny< 0 or ny>=m:
#             continue
#         if campus[nx][ny] != 'X' and not visited[nx][ny]:
#             if campus[nx][ny] == 'P':
#                 num += 1
#             dfs(campus,nx,ny,visited)


dfs(campus,posX,posY,visited)
if num == 0:
    print("TT")
else:
    print(num)



# 3 5
# OOOPO
# OIOOX
# OOOXP       # 1

# 3 3
# IOX
# OXP
# XPP         # TT
