# N과 M (9)
# n개의 자연수와 자연수 m가 주어졌을 때 조건을 만족하는 길이가 m인 수열을 모두 출력
# 조건 : n개의 자연수 중에서 m개를 고른 수열

# 입력 : n,m(1~8)
# n개의 수 (1~10000)
# 출력 : 한줄에 하나씩 문제의 조건을 만족하는 수열 출력
    # 수열 : 사전순으로 증가하는 순서로 출력, 중복되는 수열 여러번X, 각 수열은 공백으로

# 순열
# 1차 시도 : 18% 에서 시간초과

import sys

n,m = map(int,sys.stdin.readline().split())
graph = list(map(int,sys.stdin.readline().split()))
graph.sort()
visited = [False]*n

def backtracking(arr,pre):

    if len(arr) == m:
        print(*arr,sep=" ")
        return
    pre = -1
    for i in range(n):
        if visited[i] == False and pre!= graph[i] :
            pre = graph[i]
            visited[i] = True
            backtracking(arr + [graph[i]],pre)
            visited[i] = False

backtracking([],-1)

# 3 1
# 4 4 2
# #
# 2
# 4

# 4 2
# 9 7 9 1
# #
# 1 7
# 1 9
# 7 1
# 7 9
# 9 1
# 9 7
# 9 9

# 4 4
# 1 1 1 1
# #
# 1 1 1 1

# 시간초과 : 아래 반례를 넣었을 때 시간 보기
# 8 8
# 1 2 3 4 5 6 7 8