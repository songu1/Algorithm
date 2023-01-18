# N * M 크기의 얼음틀 : 구멍 O:0, 칸막이 :1
# 상하좌우끼리 붙어있는 경우 서로 연결이라 간주
# 얼음틀 모양 -> 생성되는 총 아이스크림 개수

# 첫째줄에 얼음 틀의 세로길이 N, 가로길이 M이 주어짐
# 두번째 줄부터 얼음틀의 형태 주어짐

# 출력 : 한번에 만들 수 있는 아이스크림 개수 출력

# BFS 사용

# 강의 교재 조금 참고함

import sys

icemap=[]

# 입력
N,M=map(int,sys.stdin.readline().split())

for i in range(N):
    icemap.append(list(map(int,sys.stdin.readline().rstrip())))

# DFS 함수
def dfs(map,x,y):
    # 주어진 범위 밖이면 즉시 종료
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    # 현재 노드를 방문하지 않았다면
    if map[x][y]==0:
        # 방문 처리
        map[x][y]=1
        # 상하좌우 위치도 모두 재귀적으로 호출
        dfs(map,x-1,y)
        dfs(map,x+1,y)
        dfs(map,x,y-1)
        dfs(map,x,y+1)
        return True
    return False

# main 코드
res=0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 dfs 수행
        if dfs(icemap,i,j)==True:
            res+=1

print(res)

# 4 5
# 00110
# 00011
# 11111
# 00000             # 3

# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111    # 8