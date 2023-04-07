# 치킨 배달
# 크기가 n*n인 도시 (빈칸, 치킨집, 집) - (r,c) 1부터 시작
# 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리(집을 기준으로 정해지며 각 집은 치킨거리를 가지고 있음)
# 도시의 치킨 거리 : 모든 집의 치킨 거리의 합
# (r1,c1)과 (r2,c2) 사이의 거리 = |r1-r2|+|c1-c2|
# 0:빈칸, 1:집, 2:치킨집
# 도시에서 가장 수익을 많이 낼 수 있는 치킨집의 개수 m개, 최대 m개를 고르고 나머지 폐업
# 어떻게 고르면 도시의 치킨거리가 가장 작게 될지
# 입력 : n(2~50), m(1~13)
# n개의 줄에 도시의 정보 (집의 개수 1~2n, 치킨집의 개수 m~13)
# 출력 : 폐업시키지 않을 치킨집 최대 m개를 골랐을 때 도시의 치킨거리의 최소값

import sys
from itertools import *

n,m=map(int,sys.stdin.readline().split())
graph=[]
house=[]
chicken=[]
result=9999999
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        if graph[i][j]==1:
            house.append((i+1,j+1))
        elif graph[i][j]==2:
            chicken.append((i+1,j+1))


def minDistance(house,chicken):
    distance=[]
    minValue=2*n
    for h in house:
        for c in chicken:
            minValue=min(minValue,abs(h[0]-c[0])+abs(h[1]-c[1]))
        distance.append(minValue)
        minValue=2*n
    return sum(distance)

if len(chicken)==m:
    result=minDistance(house,chicken)
else:
    chickenList=list(combinations(chicken,m))
    for c in chickenList:
        result=min(result,minDistance(house,c))

print(result)


# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2       # 5

# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2       # 10

# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0       # 11

# 5 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1       # 32