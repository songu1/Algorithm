# 파티
# n개의 숫자로 구분된 각각의 마을
# n명의 학생이 x번 마을에 모여서 파티
# 마을 사이 m개의 단방향 도로, i번째 길을 지나는데 ti(1~100)시간 소비
# 최단시간에 오고 가기를 원함
# 단방향 -> 오고 가는길이 다름
# n명의 학생들 중 오고가는데 가장 많은 시간을 소비하는 학생

# 입력 : n(1~1000), m(1~10000), x
# m개의 줄에 i번째 도로의 시작점, 끝점, 소요시간
    # 시작점과 끝점은 다름, a도시->b도시 도로는 최대 1개
    # 모든 학생들은 집에서 x에 갈수있고 x에서 집으로 돌아올수있는 데이터만 입력
# 출력 : n명의 학생 중 오고가는데 가장 오래걸리는 학생의 소요시간

import sys
import heapq

INF = int(1e9)
n,m,x = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,t = map(int,sys.stdin.readline().split())
    graph[a].append((b,t))
# print(graph)

# 다익스트라 함수
def dijkstra(start):
    dist = [INF]*(n+1)
    q = []
    # 시작노드
    heapq.heappush(q,(0,start))
    dist[start] = 0
    while q:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        time, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 잇는 노드라면
        if dist[now] < time:
            continue
        # 현재노드와 인접한 노드 확인
        for next in graph[now]:
            cost = time + next[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < dist[next[0]]:
                dist[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))
    return dist

maxTime = -1
arrive = dijkstra(x)
for k in range(1,n+1):
    if k != x:
        depart = dijkstra(k)
        total = depart[x] + arrive[k]
        maxTime = max(maxTime,total)
print(maxTime)



# 4 8 2
# 1 2 4
# 1 3 2
# 1 4 7
# 2 1 1
# 2 3 5
# 3 1 2
# 3 4 4
# 4 2 3       # 10