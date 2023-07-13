# ABCDE
# 알고리즘 캠프 n명 참가(0 ~ n-1번)
# 친구 관계
    # A-B
    # B-C
    # C-D
    # D-E
# 위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램

# 입력 : 사람의 수 (5~2000), 친구 관계의 수(1~2000)
# 정수 a,b(친구) - 같은 친구 관계가 두번 이상 주어지지 않음
# 출력 : 문제의 조건에 맞는 관계가 존재하면 1 아니면 0

import sys
n,m = map(int,sys.stdin.readline().split())
relationship = [[] for _ in range(n)]
visited = [False]*n
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    relationship[a].append(b)
    relationship[b].append(a)

# dfs 함수
def dfs(relationship,v,visited,count):
    if count == 5:
        return True
    # 방문 처리
    visited[v] = True
    for i in relationship[v]:
        if not visited[i]:
            if dfs(relationship,i,visited, count+1):
                return True
            visited[i] = False
    return False

result = 0
for i in range(n):
    if dfs(relationship,i,visited,1):
        result = 1
        break
    visited = [False]*n
print(result)

# 5 4
# 0 1
# 1 2
# 2 3
# 3 4     # 1

# 5 5
# 0 1
# 1 2
# 2 3
# 3 0
# 1 4     # 1

# 6 5
# 0 1
# 0 2
# 0 3
# 0 4
# 0 5     # 0

# 8 8
# 1 7
# 3 7
# 4 7
# 3 4
# 4 6
# 3 5
# 0 4
# 2 7     # 1