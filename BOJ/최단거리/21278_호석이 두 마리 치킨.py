# 호석이 두 마리 치킨
# 도시 안에 2개의 매장
# 도시는 n개의 건물(1~n)과 m개의 도로(건물 ai와 bi를 1시간에 양방향 이동 가능한 도로)
# 모든 건물에서의 접근성의 합을 최소화하는 2건물에 치킨집을 엶
# 건물 x의 접근성 : x에서 가장 가까운 호석이 두마리 치킨집까지 왕복하는 최단시간
# 모든 건물에서 가장 가까운 치킨집까지 왕복하는 최단시간의 총합을 최소화하는 건물 2개 선택
# (최적 위치 건물 2개 번호, 모든 건물에서 가장 가까운 치킨집까지 왕복하는 최단시간의 총합)
    # 여러개 -> 건물번호 중 작은것, 큰 것이 작을수록

# 입력 : 건물개수 n (2~100), 도로 개수 m(n-1 ~ n(n-1)/2)
# 도로의 정보 ai,bi (도로 중복 불가, 어떤 두 건물을 잡아도 도로를 따라 오고가는 방법 존재)
# 출력 : 지어질 건물 번호 2개 오름차순 , 모든 도시에서의 왕복 시간 합

# 1차 시도 : 부분 통과 (10/19)
# 2차 시도 : 전체 통과 - minD값은 최소 접근성의 합이므로 INF가 아니라 INF*n으로 설정해줘야함

import sys
from itertools import *

INF = 101
n,m = map(int,sys.stdin.readline().split())
city = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    city[a][b] = 1
    city[b][a] = 1
for i in range(1,n+1):
    city[i][i] = 0

# 플로이드 워셜
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            city[i][j] = min(city[i][j], city[i][k] + city[k][j])

chicken = list(combinations([i for i in range(1,n+1)],2))
loc = (0,0)
minD = INF*n
for (a,b) in chicken:
    distance = 0
    for i in range(1,n+1):
        distance += min(city[a][i],city[b][i])
    if distance < minD:
        minD = distance
        loc = (a,b)

print(loc[0], loc[1], minD*2)


# 5 4
# 1 3
# 4 2
# 2 5
# 3 2     # 1 2 6