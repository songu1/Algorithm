# 해킹
# yum3가 해킹, 서로 의존하는 컴퓨터들은 점차 하나 둘 전염됨
# a가 b에 의존 : b -> a 감염 (일방향)
# yum3이 해킹한 컴퓨터 번호와 의존성 -> 해킹당한 컴퓨터까지 포함하여 총 몇대의 컴퓨터가 감염, 걸리는 시간

# 입력 : 테스트케이스 수 t (1~100)
# 컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터 번호 c
# d개의 줄에 의존성을 나타내는 정수 a, b, s (a가 b를 의존, b감염시 s초 후 a 감염)
    # 같은 의존성은 한번만
# 출력 : 각 테스트 케이스마다 한줄에 걸쳐 감염되는 컴퓨터수, 마지막 컴퓨터가 감염되기까지 걸리는 시간

import sys
import heapq

def dijkstra(start):
    q = []
    # 시작노드 최단경로 설정
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 이미 방문한 노드라면 무시
        if distance[now] < dist:
            continue
        # 인접 컴퓨터 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 이동할 때가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


INF = int(1e9)
tc = int(sys.stdin.readline())
for _ in range(tc):
    n, d, c = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF]*(n+1)
    for _ in range(d):
        a,b,s = map(int,sys.stdin.readline().split())
        graph[b].append((a,s))
    dijkstra(c)
    count = 0
    maxDist = -1
    for dist in distance:
        if dist != INF:
            count += 1
            maxDist = max(maxDist,dist)
    print(count, maxDist)
        
    
# 2
# 3 2 2
# 2 1 5
# 3 2 5
# 3 3 1
# 2 1 2
# 3 1 8
# 3 2 4
# #
# 2 5
# 3 6