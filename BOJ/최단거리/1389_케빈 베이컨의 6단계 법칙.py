# 케빈 베이컨의 6단계 법칙
# 지구에 있는 모든 사람들은 최대 6단계 이내에서 서로 아는 사람으로 연결 가능
# 임의의 두 사람이 최소 몇 단계만에 이어질 수 있는지 계산하는 게임
# 케빈 베이컨의 수 : 모든 사람과 케빈 베이컨 게임을 했을 때 나오는 단계의 합
# 유저수, 친구관계 -> 케빈 베이컨의 수가 가장 작은 사람을 구하는 프로그램
# 사람 번호 1~n

# 입력 : 유저의 수 n(2~100) , 친구 관계의 수 m(1~5000)
# 친구 관계 : 친구 관계가 중복되어 들어올 수 O, 친구 관계가 없는 사람 없음, 모든 사람이 연결됨
# 출력 : 케빈 베이컨의 수가 가장 작은 사람 (여러명일 경우 번호가 가장 작은 사람)

import sys
INF = 999

# 입력
n,m = map(int,sys.stdin.readline().split())
# relationship = [[] for _ in range(n+1)]
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    # relationship[a].append(b)
    # relationship[b].append(a)
    graph[a][b] = 1
    graph[b][a] = 1
# 자기 자신에서 자기 자신으로
for i in range(1,n+1):
    graph[i][i] = 0
# 임시 출력

# 플로이드 워셜 알고리즘
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,i):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            graph[j][i] = graph[i][j]

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("%4d"%graph[i][j],end=" ")
#     print()

# 케빈 베이컨 수 출력
minSum = 999999
result = 0
for i in range(1,n+1):
    stepSum = sum(graph[i]) - 999
    if stepSum < minSum:
        minSum = stepSum
        result = i
print(result)

# 5 5
# 1 3
# 1 4
# 4 5
# 4 3
# 3 2     # 3