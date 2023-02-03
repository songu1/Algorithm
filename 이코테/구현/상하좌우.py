# 여행가 N*N 크기의 정사각형 공간 위 (1*1 크기 정사각형)
# (1,1)~(N,N)
# 상하좌우 방향으로 정사각형내에서 이동, 시작좌표 (1,1)
# L: 왼쪽 / R: 오른쪽 / U: 위 / D: 아래
# 도착 지점의 좌표는?

# 첫째줄 : 공간의 크기 n (1<=N<=100)
# 둘째줄 : a가 이동할 계획서 (1<=이동횟수<=100)

# 요구사항대로 충실하면 되는 문제
# 시뮬레이션 유형


n=int(input())
paths=list(map(str,input().split()))
x,y=1,1
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for path in paths:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if path==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
        
    if nx<1 or ny<1 or nx>n or ny>n:
            continue
    # 이동 수행
    x,y=nx,ny

print(x,y)



# 5
# R R R U D D           #3 4