# 크기 n*n인 그리디에 RGB 중 하나 색칠
# 구역은 같은색 - 몇개의 구역
# 같은 색상이 상하좌우로 인접 -> 같은 구역
# 적록색약이아닌 사람 인접한 R,G,B로 구역의 수
# 적록색약인 사람 인접한 RG,B로 구역의 수
# 적록색약인 사람이 봤을 때 ,아닌 사람이 봣을 때 구역의 수

# 입력 : n
# n개의 줄에 그림이 주어짐

# 출력 : 적록색약이 아닌 경우 구역의 수 / 적록색약인 사람 구역의 수

import sys
sys.setrecursionlimit(10000)
# 입력
n=int(sys.stdin.readline())

picX=[]
picO=[[] for _ in range(n)]
for i in range(n):
    picX.append(list(map(str,sys.stdin.readline().rstrip())))
    for j in range(n):
        if picX[i][j]=='G':
            picO[i].append('R')
        else:
            picO[i].append(picX[i][j])
    

resX=0
resO=0

# dfs 함수
def dfs(pic,x,y,color):
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if pic[x][y]=='O':
        return False
    elif pic[x][y]==color:
        pic[x][y]='O'
        dfs(pic,x-1,y,color)
        dfs(pic,x+1,y,color)
        dfs(pic,x,y-1,color)
        dfs(pic,x,y+1,color)
        return True
    return False

# main 코드
for i in range(n):
    for j in range(n):
        if dfs(picX,i,j,picX[i][j])==True:
            resX+=1
        if dfs(picO,i,j,picO[i][j])==True:
            resO+=1

print(resX,resO)

# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR       # 4 3