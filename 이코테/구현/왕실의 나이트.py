# 왕실 정원 : 8*8 좌표 평면
# 특정한 한 칸 : 나이트가 서있음(말을 타고 있음)
# 이동시 L자 형태로만 이동, 정원 밖 이동 불가능
# 이동 :  수평으로 2칸, 수직 1칸 / 수직으로 2칸, 수평 1칸
# 나이트의 위치가 주어졌을 때 나이트가 이동할 경우의 수
# 행위치 : 1~8, 열위치 a~h

# 입력 : 열행
# 출력 : 나이트가 이동할 수 있는 경우의 수

import sys

row=[]
col=[0,'a','b','c','d','e','f','g','h']

c,r=map(str,sys.stdin.readline().rstrip())

r=int(r)
c=ord(c)-96     # a의 아스키코드값이 97이므로

dr=[2,2,-2,-2,1,1,-1,-1]
dc=[1,-1,1,-1,2,-2,2,-2]

count=0

for i in range(8):
    nr=r+dr[i]
    nc=c+dc[i]
    if nr>=1 and nr<=8 and nc>=1 and nc<=8:
        count+=1
    

print(count)

# a1        # 2
# c2        # 6