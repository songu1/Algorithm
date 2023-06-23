# 플로이드
# n개의 도시(2~100)
# 한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스(1~100,000)
# 각 버스는 한번 사용할 때 필요한 비용이 있음
# 모든 도시의 쌍(A,B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값

# 입력 : 도시 개수 n
# 버스 개수 m
# 버스의 정보(시작도시 a, 도착 도시 b, 비용 c) - a!=b , c(1~100,000)
    # 시작도시와 도착도시를 연결하는 노선은 하나가 아닐 수 있음!(*************중요**************)
# 출력 : n개의 줄에 i에서 j로 가는데 필요한 최소비용 출력 (없으면 0)


import sys
INF = int(1e9)

# 입력
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
graph=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

# 자기 자신에서 자기 자신으로 가는 비용
for i in range(1,n+1):
    graph[i][i] = 0

# 플로이드 워셜 알고리즘
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        # 도달할 수 없을 때
        if graph[i][j] == INF:
            print(0, end=" ")
        else:  
            print(graph[i][j], end=" ")
    print()


# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4
# #
# 0 2 3 1 4
# 12 0 15 2 5
# 8 5 0 1 1
# 10 7 13 0 3
# 7 4 10 6 0