# 여행가 N*N 크기의 정사각형 공간 위 (1*1 크기 정사각형)
# (1,1)~(N,N)
# 상하좌우 방향으로 정사각형내에서 이동, 시작좌표 (1,1)
# L: 왼쪽 / R: 오른쪽 / U: 위 / D: 아래
# 도착 지점의 좌표는?

# 첫째줄 : 공간의 크기 n (1<=N<=100)
# 둘째줄 : a가 이동할 계획서 (1<=이동횟수<=100)

# 5
# R R R U D D           #3 4

N=int(input())
path=list(map(str,input().split()))



print(path)