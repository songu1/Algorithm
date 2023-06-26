# N과 M (1)
# 자연수 n,m -> 1~n까지 자연수 중에서 중복 없이 m개를 고른 수열

# 입력 : 자연수 n,m(1~8)
# 출력 : 한줄에 하나씩 문제의 조건을 만족하는 수열
    # 중복되는 수열 여러번X, 각 수열은 공백으로 구분, 사전순

import sys

n,m = map(int,sys.stdin.readline().split())
arr = [i+1 for i in range(n)]
visited = [False]*n

def backtracking(array):
    if len(array) == m:
        print(*array,sep=" ")
        return
    for i in range(len(arr)):
        if visited[i] == False:
            visited[i] = True
            backtracking(array + [arr[i]])
            visited[i] = False

backtracking([])



# 3 1
# #
# 1
# 2
# 3

# 4 2
# #
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3

# 4 4
# #
# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
# 2 1 4 3
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
# 2 4 3 1
# 3 1 2 4
# 3 1 4 2
# 3 2 1 4
# 3 2 4 1
# 3 4 1 2
# 3 4 2 1
# 4 1 2 3
# 4 1 3 2
# 4 2 1 3
# 4 2 3 1
# 4 3 1 2
# 4 3 2 1