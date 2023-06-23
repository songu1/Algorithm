# 지름길
# D킬로미터의 고속도로 : 심각하게 커브가 많아서 운전하기 힘듦
# 지름길 : 일방통행 / 고속도로 : 역주행 불가능
# 세준이가 운전해야하는 거리의 최솟값

# 입력 : 지름길 개수 n(1~12), 고속도로의 길이 D(1~10000)
# 지름길의 시작위치, 도착위치, 지름길 길이 (1~10000)
    # 지름길 시작위치는 도착위치보다 작음
# 출력 : 세준이가 운전해야하는 거리의 최솟값

# 실패1 : 12%에서 틀림

import sys
import heapq

n, d = map(int,sys.stdin.readline().split())
q = []
distance = [i for i in range(d+1)] 

# 모든 지름길 정보 입력 받기
for _ in range(n):
    a,b,c =  map(int,sys.stdin.readline().split())
    if a <= d and b <= d:
        heapq.heappush(q,(a,b,c))

def dijkstra():
    # print("dijkrstra")
    while q:
        # 가장 앞의 위치와 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        a,b,c = heapq.heappop(q)
        # print(a,b,c)
        if distance[b] < distance[a] + c:
            continue
        distance[b] = distance[a] + c
        # 현재 노드와 연결된 다른 인접한 노드 확인
        k = 0
        for i in range(b+1,d+1):
            k += 1
            distance[i] = min(distance[i], distance[b] + k)

# 다익스트라 알고리즘 수행
dijkstra()
# print(distance)

# 최단거리 출력
print(distance[d])


# 5 150
# 0 50 10
# 0 50 20
# 50 100 10
# 100 151 10
# 110 140 90      # 70

# 2 100
# 10 60 40
# 50 90 20        # 80

# 8 900
# 0 10 9
# 20 60 45
# 80 190 100
# 50 70 15
# 160 180 14
# 140 160 14
# 420 901 5
# 450 900 0       # 432

# 내가 만든 반례
# 2 50
# 10 40 10
# 20 30 9         # 30