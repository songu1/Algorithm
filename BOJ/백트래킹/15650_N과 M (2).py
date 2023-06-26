# N과 M (2)
# (1) 1~n까지 중복없이 m개
# (2) 고른 수열이 오름차순
# -> 조합

import sys

n,m = map(int,sys.stdin.readline().split())
array = [i+1 for i in range(n)]

def backtracking(arr,idx):
    if len(arr) == m:
        print(*arr, sep=" ")
        return
    for i in range(idx,n):
        backtracking(arr + [array[i]], i+1)

backtracking([],0)



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
# 2 3
# 2 4
# 3 4

# 4 4
# #
# 1 2 3 4