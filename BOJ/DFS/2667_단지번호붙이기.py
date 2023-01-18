# 단지번호 붙이기 (음료수 얼려먹기와 비슷)
# 지도 1:집이 있는 곳 / 0:집이 없는곳
# 연결된 집의 모임인 단지를 정의하고 단지에 번호 붙이기
# 단지수 출력, 각 단지에 속하는 집의 수를 오름차순으로 출력

# 입력: 지도의 크기 n(정사각형)
# n개의 자료(지도)

# 출력 : 총 단지 수
# 각 단지내 집의 수를 오름차순으로 정렬

# 글로벌 함수 c 사용하여 단지별 개수 계산 -> 시간 축소 가능

import sys

n=int(sys.stdin.readline().rstrip())
maze=[]

for i in range(n):
    maze.append(list(map(int,sys.stdin.readline().rstrip())))

# dfs 함수
def dfs(maze,x,y,c):
    # 주어진 범위 밖 - 지도가 나올땐 꼭 체크해주기!
    if x<0 or y<0 or x>=n or y>=n:
        return False
    if maze[x][y]==1:
        # 방문처리
        maze[x][y]=c    # 단지당 번호 부여
        # 재귀적으로 처리
        dfs(maze,x-1,y,c)
        dfs(maze,x+1,y,c)
        dfs(maze,x,y-1,c)
        dfs(maze,x,y+1,c)
        return True
    return False

# 번호 매기기
res=0
count=[]
for i in range(n):
    for j in range(n):
        if dfs(maze,i,j,res+2)==True:
            res+=1
# 출력           
print(res)
for i in range(res):
    c=0
    for j in range(n):
        c+=maze[j].count(i+2)
    count.append(c)
count.sort()
print(*count,sep='\n') # 리스트를 줄 바꿔 출력


# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
# 
# 3
# 7
# 8
# 9