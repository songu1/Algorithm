# 자물쇠(lock) : n*n 격자형태 (홈이 파여있음)
# 특이 모양 열쇠(key) : m*m 격자형태 (홈과 돌기 부분이 있음)
# 열쇠 : 회전과 이동이 가능
# 열쇠의 돌기 부분이 자물쇠의 홈부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈 돌기는 영향X
# 자물쇠 영역내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야함
# 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야함
# key와 lock의 원소는 0(홈) 또는 1(돌기)로 이루어져있음

import sys
key=[]
key=map(list,sys.stdin.readline())

print(key)







# [[0,0,0],[1,0,0],[0,1,1]]
# [[1,1,1],[1,1,0],[1,0,1]]         # true