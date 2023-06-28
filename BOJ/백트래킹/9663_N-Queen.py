# N Queen
# n*n 체스판 위 퀸 n개를 서로 공격할 수 없게 놓는 문제
# n -> 퀸을 놓는 방법의 수
# 공격할 수 없는 조건 : 퀸의 일직선 밑 대각선에 아무것도 놓이면 안됨

# 입력 : n (1~14)
# 출력 : 퀸 n개를 서로 공격할 수 없게 놓는 경우의 수를 출력

# 풀이 : n*n개 칸에서 n개를 뽑음 -> 일직선, 대각선으로 서로 겹치면 안됨

import sys
n = int(sys.stdin.readline())
graph = [[0]*n for _ in range(n)]
case = 0

def invalid(x,y,valid):
    # 세로
    for i in range(n):
        valid[i][y] = False
    # 가로
    for j in range(n):
        valid[x][j] = False
    # 대각선 \
    i = x
    for j in range(y+1,n):
        i += 1
        if i>=n: break
        valid[i][j] = False
    # 대각선 /
    i = x
    for j in range(y-1,-1,-1):
        i += 1
        if i >= n: break
        valid[i][j] = False
    return valid


def backtracking(x,y,arr,valid):
    global case
    graph[x][y] = 1
    valid = invalid(x,y,valid)
    # print(valid)
    if len(arr) == n:
        case += 1
        # print(arr)
        return
    nx = x + 1
    if nx >= n: return
    for ny in range(n):
        if valid[nx][ny] == True:
            valid2 = [valid[i][:] for i in range(n)]
            backtracking(nx, ny, arr + [(nx,ny)], valid2)
            graph[nx][ny] = 0 
    return

valid = [[True]*n for _ in range(n)]

for j in range(n):
    backtracking(0,j,[(0,j)],valid)
    graph[0][j] = 0
    valid = [[True]*n for _ in range(n)]

print(case)

# def backtracking2(x,y,arr):
#     global case
#     graph[x][y] = 1
#     if len(arr) == n:
#         case += 1
#         # print(arr)
#         return
#     nx = x + 1
#     if nx >= n: return
#     for ny in range(n):
        


#         if valid[nx][ny] == True:
#             valid2 = [valid[i][:] for i in range(n)]
#             backtracking(nx, ny, arr + [(nx,ny)], valid2)
#             graph[nx][ny] = 0 
#     return

# 8       # 92