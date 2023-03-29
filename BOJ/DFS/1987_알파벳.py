# 알파벳 - DFS
# **** DFS로 풀꺼면 pypy로 제출 / BFS로 풀꺼면 Python3로 제출 ******
    # pypy 메모리 초과 : setrecursionlimit 지우기
# 세로 R칸, 가로 c칸으로 된 표 모양의 보드
# 보드의 각 칸에 대문자 알파벳, 1행열에는 말이 놓여있음
# 말은 상하좌우로 인접한 칸으로 이동가능
# 지금까지 지나온 칸의 알파벳과 다른 칸으로 이동해야함 (같은 알파벳 2번 이상X)
    # 출발지 포함
# 좌측상단(1행1열)부터 말이 최대 몇칸을 지날 수 있는지

# 입력 : 세로, 가로 R,C(1~20)
# R개의 줄에 C개의 대문자 알파벳
# 출력 : 말이 지날 수 있는 최대의 칸 수

# 구상 : dict이용하여 알파벳 방문한지 체크 
    # -> 딕셔너리는 best이면 O(1)이지만 worst는 O(n)
    # dict는 매우 느림(일반 리스트를 사용하는 것이 빠름) - 지수복잡도는 매우 빠르게 증가
    # list에 원소들을 순차적으로 넣고 순차적으로 탐색하는 것보다는 dict가 빠르지만 동알하게 접근한다면 리스트가 훨씬 빠름
# 구상2 : dict 대신 ord로 인덱스 설정하여 풀기 (ord(문자)-65)를 인덱스로 지정하기 -> 66에서 메모리 초과

import sys

# 입력
r,c=map(int,sys.stdin.readline().split())
graph=[]
checked=[False]*26
for i in range(r):
    graph.append(list(map(str,sys.stdin.readline().rstrip())))
result=0

# DFS 함수
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(graph,x,y,count):
    global result
    # 방문처리
    checked[ord(graph[x][y])-65]=True
    count+=1
    for j in range(4):
        nx=x+dx[j]
        ny=y+dy[j]
        if 0<=nx<r and 0<=ny<c and checked[ord(graph[nx][ny])-65]==False:
            dfs(graph,nx,ny,count)
    # 경로의 최대 칸 수 result에 저장
    result=max(result,count)
    checked[ord(graph[x][y])-65]=False
    count-=1
    return result

# main 코드
print(dfs(graph,0,0,0))


# 사전을 이용한 풀이 (시간 초과)

# # 입력
# r,c=map(int,sys.stdin.readline().split())
# graph=[]
# check=dict()
# for i in range(r):
#     graph.append(list(map(str,sys.stdin.readline().rstrip())))
#     for j in range(c):
#         if graph[i][j] not in check.keys():
#             check[graph[i][j]]=False
# result=[]

# # DFS함수
# def dfs(graph,x,y,count):
#     # 주어진 범위 외 return
#     if x<0 or x>=r or y<0 or y>=c:
#         return False
#     # 아직 방문하지 않은 알파벳을 만났을 경우
#     if check[graph[x][y]]==False:
#         # 방문처리
#         check[graph[x][y]]=True
#         count+=1
#         dfs(graph,x-1,y,count)
#         dfs(graph,x+1,y,count)
#         dfs(graph,x,y-1,count)
#         dfs(graph,x,y+1,count)
#         # 경로의 칸 수 result 리스트에 저장
#         result.append(count)
#         check[graph[x][y]]=False
#         count-=1
#         return True
#     # 이미 방문한 알파벳
#     return False

# # main 코드
# dfs(graph,0,0,0)
# print(max(result))


# 2 4
# CAAB
# ADCB        # 3

# 3 6
# HFDFFB
# AJHGDH
# DGAGEH      # 6

# 5 5
# IEFCJ
# FHFKC
# FFALF
# HFGCF
# HMCHH       # 10