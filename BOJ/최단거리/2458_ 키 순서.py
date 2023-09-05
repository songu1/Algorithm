# 키 순서 : 풀이 참고
# 1~n 번호가 붙여져 있는 학생 -> 두 학생끼리 키를 비교한 결과
# n명 학생 키는 모두 다름
# a번 학생 < b번 학생 : a->b
# 학생들의 키를 비교한 결과 -> 자신의 키가 몇번째인지 알 수 있는 학생이 모두 몇명인지 계산

# 입력 : 학생 수 n (2~500), 두학생 키를 비교한 횟수 m
# m개ㅡ이 줄에 두 학생의 키를 비교한 결과를 나타내는 양의 정수 a,b
    # a < b
# 출력 : 자신이 키가 몇번째인지 알수있는 학생이 모두 몇명인지

# 플로이드 워셜 : k - i - j 순서임!! 기억하기
# 1차시도 - 시간초과 실패 : dfs로 모두 연결되었는지 확인 + 연결되었다면 플로이드 워셜로 모두로 가거나 모두에서 오는 0, n+1 추가 후 최장거리 탐색
# 2차시도 - 실패 :플로이드 워셜로 모두로 가거나 모두에서 오는 0, n+1 추가 후 최장거리 탐색 (0번 행과 n+1열에서 겹치지 않는 것 선택)
# 3차시도 - python3 시간초과 / pypy3 성공 : 플로이드 워셜로 최단거리 탐색하여 갈 수 있는 위치인지 확인하고 모든 학생과 오고가고가 되면 count하기

# 자신의 순위를 확인할 수 있는지 -> 자신에서 출발, 자신으로 도착하는 수를 count하여 모든 곳와 이동이 가능하면 순위를 알 수 있음 *********
    # dfs로 갈 수 있는 노드인지 확인
    # 플로이드 워셜로 최단거리를 구해 갈 수 있는지 확인

import sys

# 플로이드 워셜 방법
INF = int(1e9)
n,m = map(int,sys.stdin.readline().split())
distance = [[INF]*(n+1) for _ in range(n+1)]    # 최장 거리 구하기 위한 배열
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    distance[a][b] = 1

# 최단 거리 구하기
for i in range(1,n+1):
    distance[i][i] = 0

# 플로이드 워셜 - 1~n+1로
for k in range(1,n+1):      
    for i in range(1,n+1):
        for j in range(1,n+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

# 출력
connect = [0]*(n+1)
for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j] != INF and distance[i][j] != 0:
            connect[i] += 1
            connect[j] += 1
count = 0
for i in range(1,n+1):
    if connect[i] == n-1:
        count += 1

print(count)


# 6 6
# 1 5
# 3 4
# 5 4
# 4 2
# 4 6
# 5 2             # 1

# 6 7
# 1 3
# 1 5
# 3 4
# 5 4
# 4 2
# 4 6
# 5 2             # 2

# 6 3
# 1 2
# 2 3
# 4 5             # 0