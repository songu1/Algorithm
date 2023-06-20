# 최단경로
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램
# 모든 간선의 가중치는 10 이하의 자연수
# 모든 정점에는 1부터 v까지 번호가 매겨져 있음
# 자기 자신에게 가는 간선은 없음
# 서로 다른 두 정점 사이에 여러개의 간선이 존재할 수 있음

# 입력 : 정점의 개수 v, 간선의 개수 e (1~20000 / 1~300000)
# 시작 정점의 번호 k
# e개의 줄에 걸쳐 각 간선을 나타내는 정수 u,v,w (u->v 가중치 w) w:1~10
# 출력 : v개 줄에 걸쳐 i번 정점으로의 최단 경로의 경로값 (시작점은 0, 경로X은 INF)

import sys
import heapq

INF = int(1e9)
# 입력
vv,e = map(int,sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph=[[] for _ in range(vv+1)]
visited=[False]*(vv+1)
distance=[INF]*(vv+1)
for i in range(e):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))

# 최단경로 함수
def dijkstra(start):
    # 시작노드 초기화
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    visited[start] = True
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1] # start에서 현재 노드를 거쳐서 가는 경우
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))


# main 코드
dijkstra(k)

for i in range(1,vv+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])



# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6
# #
# 0
# 2
# 3
# 7
# INF