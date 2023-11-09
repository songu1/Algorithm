# 퍼즐
# 3*3 표에 수가 채워져 있음, 마지막 칸은 빈칸
# 상하좌우 중 1개에 빈칸이 있으면 이동 가능
# 초기상태 -> 최소의 이동으로 1~8까지 정렬된 상태 만들기
    # 1 2 3
    # 4 5 6
    # 7 8 0
# 최소 이동 횟수 구하는 프로그램

# 입력 : 3줄에 걸쳐서 표에 채워져있는 아홉개의 수(빈칸 0)
# 출력 : 최소 이동 횟수(이동 불가능 시 -1)

# 1차시도 : 17% 실패 - 1차원 배열 경우
# 2치시도 : 92% 실패
# 3차시도 : 성공 -> 엣지케이스 꼭 테스트해보기(123456790)

import sys
from collections import deque

table = []
for i in range(3):
    table.append(list(map(str,sys.stdin.readline().split())))
    for j in range(3):
        if table[i][j] == '0':
            x,y = i,j

def listToStr(arr):
    string = ""
    for i in range(3):
        string += ''.join(arr[i])
    return string

def strToList(str):
    arr = []
    for i in range(3):
        arr.append([str[i*3], str[i*3+1], str[i*3+2]])
    return arr

dic = {}
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(table,x,y):
    queue = deque([])
    tab = listToStr(table)
    if tab == '123456780':
        return 0
    queue.append((0,-1,-1,x,y,tab))
    while queue:
        time, preX, preY, x, y, tab = queue.popleft()
        time += 1
        table = strToList(tab)
        for i in range(4):
            # 이동 가능한 위치
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3 or (nx,ny) == (preX,preY):
                continue
            # 이동한 Table 리스트에서 이동
            newTable = [table[0][:],table[1][:],table[2][:]]
            newTable[x][y], newTable[nx][ny] = newTable[nx][ny], newTable[x][y]
            newTab = listToStr(newTable)
            # 퍼즐 완료 시 return
            if newTab == '123456780':
                return time
            # 퍼즐 미완료 시
            if newTab not in dic.keys():
                dic[newTab] = time
                queue.append((time, x, y, nx, ny, newTab))
    return -1

print(bfs(table,x,y))



# 1 0 3
# 4 2 5
# 7 8 6       # 3

# 3 6 0
# 8 1 2
# 7 4 5       # -1

# 2 3 5
# 1 8 0
# 4 7 6       # 9

# 1 2 3
# 4 5 6
# 7 8 0       # 0