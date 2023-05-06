# 영역 구하기
# m*n 크기이 모눈종이 / 모눈종이 위에 눈금을 맞추어 k개의 직사각형을 그림
    # 모눈종이 왼쪽 아래 꼭지점 (0,0) -> 왼쪽 위 꼭짓점 (m,n)
# k개의 직사각형 내부를 제외한 나머지 부분이 몇개의 분리된 영역으로 나누어짐
# m,n,k,k개의 직사각형 좌표 -> k개의 직사각현 내부를 제외한 나머지 부분이 몇개의 영역으로 나누어지는지, 각 영역의 넓이가 무엇인지 계산
# x y
# n m
# c r

# 입력 : m,n,k (1~100)
# k개의 줄에 직사각형 왼쪽 아래 꼭짓점의 (x,y), 직사각형 오른쪽 위 꼭짓접의 (x,y)
# 출력 : 분리되어 나누어지는 영역의 개수
# 각 영역의 넓이를 오름차순으로 정렬하여 출력

import sys
sys.setrecursionlimit(100000)

m,n,k=map(int,sys.stdin.readline().split())
arr=[[0]*n for _ in range(m)]       # 0:빈칸, -1:직사각형, 다른 숫자 : 넓이 계산
for i in range(k):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j]=-1

# # 출력 함수(임시)
# def printArr(arr):
#     for i in range(m-1,-1,-1):
#         for j in range(n):
#             print(arr[i][j],end=' ')
#         print()

# dfs 함수
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(graph,x,y,size):
    # 넓이
    size=graph[x][y]
    # 탐색
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=m or ny>=n:
            continue
        if graph[nx][ny]==0:
            graph[nx][ny]=size+1
            size=dfs(graph,nx,ny,size)

    return size

# main 코드
area=[]
count=0
for i in range(m):
    for j in range(n):
        if arr[i][j]==0:
            arr[i][j]=1
            area.append(dfs(arr,i,j,-2))
            count+=1
area.sort()
print(count)
print(*area,sep=' ')


# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2
#
# 3
# 1 7 13