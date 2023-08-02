# 상어 초등학교
# n*n 크기의 교실에 학생 수 n^2(1~n^2번)
# (r,c) : r행 c열 (1,1) -> (n,n)
# 학생의 순서 , 각 학생이 좋아하는 학생 4명
# 배치 규칙
    # |r1-r2| + |c1-c2| = 1을 만족하는 두 칸이 인접 => 상하좌우
    # (1) 비어있는 칸 중에서 좋아하는 학생이 가장 많이 인접하는 칸으로 정함
    # (2) 1을 만족하는 칸이 여러개 -> 인접 칸 중 비어있는 칸이 가장 많은 칸
    # (3) 2를 만족하는 칸이 여러개 -> 행 번호, 열 번호 오름차순으로 자리를 정함
# 자리 배치가 끝난 후 학생의 만족도를 계산 - 인접한 칸에 좋아하는 학생 수
    # 0명-0 / 1명-1 / 2명-10 / 3명-100 / 4명-1000

# 입력 : n (3~20)
# 학생의 번호, 그 학생이 좋아하는 학생 4명의 번호 (선생님이 자리를 정할 순서대로)
    # 학생번호, 좋아하는 학생 중복X
# 출력 : 학생의 만족도의 총합

# 임시 출력
def printClass(classroom,n,s):
    print(s)
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(classroom[i][j],end=" ")
        print()

# 알고리즘
    # 1. 배치 - (1) 찾기 / (2),(3)은 같이 빈칸의 수를 구하면서 max값 저장(더 큰값이 나올때만)
    # 2. 만족도 계산
import sys

n = int(sys.stdin.readline())
classroom = [[0]*(n+1) for _ in range(n+1)]
order = []
friend = [[] for _ in range(n**2+1)]
for _ in range(n**2):
    input = list(map(int,sys.stdin.readline().split()))
    order.append(input[0])
    friend[input[0]] = input[1:]

dx = [-1,0,0,1]     # 상 좌 우 하
dy = [0,-1,1,0]

# 첫 학생 위치 설정
classroom[2][2] = order[0]
# printClass(classroom,n,order[0])
del order[0]

for s in order:
    maxFav = -1
    maxEmp = -1
    pos = [0,0]
    # 빈칸 탐색 & 위치 찾기
    for x in range(1,n+1):
        for y in range(1,n+1):
            # 빈 칸일 경우
            if classroom[x][y] == 0:
                fav = 0
                emp = 0
                # 상좌우하 주변 탐색
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 1 or nx > n or ny < 1 or ny > n:
                        continue
                    # 좋아하는 친구가 있다면
                    if classroom[nx][ny] in friend[s]:
                        fav += 1
                    # 빈칸이 있다면
                    elif classroom[nx][ny] == 0:
                        emp += 1
                # 배치할 위치 찾기
                if fav > maxFav:    # 좋아하는 친구수가 클 때
                    maxFav = fav
                    maxEmp = emp
                    pos = [x,y]
                elif fav == maxFav and emp > maxEmp: # 좋아하는 친구수가 같고 빈칸이 많을 때
                    maxEmp = emp
                    pos = [x,y]
                # 빈칸이 같은 경우는 순서대로 구현시 앞의 값
    # 배치
    classroom[pos[0]][pos[1]] = s
    # printClass(classroom,n,s)

result = 0
for x in range(1,n+1):
    for y in range(1,n+1):
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or nx > n or ny < 1 or ny > n:
                continue
            if classroom[nx][ny] in friend[classroom[x][y]]:
                count += 1
        if count == 1:
            result += 1
        elif count == 2:
            result += 10
        elif count == 3:
            result += 100
        elif count == 4:
            result += 1000
print(result)

# 3
# 4 2 5 1 7
# 3 1 9 4 5
# 9 8 1 2 3
# 8 1 9 3 4
# 7 2 3 4 8
# 1 9 2 5 7
# 6 5 2 3 4
# 5 1 9 2 8
# 2 9 3 1 4       # 54

# 3
# 4 2 5 1 7
# 2 1 9 4 5
# 5 8 1 4 3
# 1 2 9 3 4
# 7 2 3 4 8
# 9 8 4 5 7
# 6 5 2 3 4
# 8 4 9 2 1
# 3 9 2 1 4       # 1053