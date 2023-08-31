# 큐빙 - 노가다로 문제 해결
# 루빅스 큐브 3*3*3
# 각 면의 9칸이 모두 색이 동일해야함
# 양 방향을 90도씩 돌릴 수 있음 -> 회전을 마친 후 다른 면을 돌릴 수 있음
# 위:white / 아래:yellow / 앞:red / 뒤:orange / 좌:green / 우:blue
# 큐브를 돌린 방법 -> 모두 돌린 후 가장 윗면의 색상을 구하는 프로그램

# 입력 : 테스트케이스 수(1~100)
# 큐브를 돌린 횟수 n(1~1000)
# 큐브를 돌린 방법 : 돌린면 side(U,D,F,B,L,R) , 돌린 방향 dir(+시계 / -반시계)
# 출력 : 각 테스트케이스에 대해 큐브를 모두 돌린 후 윗면의 색상
    # 9칸을 3줄에 걸쳐 출력 (w,y,r,o,g,b)

import sys

# 큐브 회전 함수
def getResult(cube,side,dir):
    up, left, down, right = [],[],[],[]
    if side == 'U':
        cube[0] = spinFace(cube[0],dir)
        cube[3][0],cube[4][0],cube[2][0],cube[5][0] = spinNear(cube[3][0],cube[4][0],cube[2][0],cube[5][0],dir)
    elif side == 'D':
        cube[1] = spinFace(cube[1],dir)
        cube[3][2],cube[5][2],cube[2][2],cube[4][2] = spinNear(cube[3][2],cube[5][2],cube[2][2],cube[4][2],dir)
    elif side == 'F':
        for i in range(3):
            left.append(cube[4][2-i][2])
            right.append(cube[5][i][0])
        cube[0][2], left, cube[1][2], right = spinNear(cube[0][2],left,cube[1][2],right,dir)
        for i in range(3):
            cube[4][2-i][2] = left[i]
            cube[5][i][0] = right[i]
    elif side == 'B':
        cube[3] = spinFace(cube[3],dir)
        for i in range(3):
            left.append(cube[5][i][2])
            right.append(cube[4][2-i][0])
        cube[0][0],left,cube[1][0],right = spinNear(cube[0][0],left,cube[1][0],right,dir)
        for i in range(3):
            cube[5][i][2] = left[i]
            cube[4][2-i][0] = right[i]
    elif side == 'L':
        cube[4] = spinFace(cube[4],dir)
        for i in range(3):
            up.append(cube[0][i][0])
            left.append(cube[3][2-i][2])
            down.append(cube[1][2-i][2])
            right.append(cube[2][i][0])
        up,left,down,right = spinNear(up,left,down,right,dir)
        for i in range(3):
            cube[0][i][0] = up[i]
            cube[3][2-i][2] = left[i]
            cube[1][2-i][2] = down[i]
            cube[2][i][0] = right[i]
    else:
        cube[5] = spinFace(cube[5],dir)
        for i in range(3):
            up.append(cube[0][i][2])
            left.append(cube[2][i][2])
            down.append(cube[1][2-i][0])
            right.append(cube[3][2-i][0])
        up,left,down,right = spinNear(up,left,down,right,dir)
        for i in range(3):
            cube[0][i][2] = up[i]
            cube[2][i][2] = left[i]
            cube[1][2-i][0] = down[i]
            cube[3][2-i][0] = right[i]

# 평면 회전
def spinFace(cubeOne,dir):
    face = [['']*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if dir=='+':
                face[i][j] = cubeOne[2-j][i]
            else:
                face[i][j] = cubeOne[j][2-i]
    return face

# 평면 주위 회전
def spinNear(up,left,down,right,dir):
    if dir == '+':
        up,left,down,right = left,down,right,up
    else:
        up,left,down,right = right,up,left,down
    return up,left,down,right
    
# main 코드
tc = int(sys.stdin.readline())

for _ in range(tc):
    n = int(sys.stdin.readline())
    way = list(map(str,sys.stdin.readline().split()))
    cube = [[[i]*3 for _ in range(3)] for i in ['w','y','r','o','g','b']]
    for w in way:
        side, dir = w[0], w[1]
        getResult(cube,side,dir)
    
    # 출력
    for i in range(3):
        print(*cube[0][i],sep="")

# 4
# 1
# L-
# 2
# F+ B+
# 4
# U- D- L+ R+
# 10
# L- U- L+ U- L- U- U- L+ U+ U+
# #
# rww
# rww
# rww
# bbb
# www
# ggg
# gwg
# owr
# bwb
# gwo
# www
# rww