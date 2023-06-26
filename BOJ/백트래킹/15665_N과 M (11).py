# N과 M (11)
# (1) N개의 자연수 중에서 M개를 고른 수열
# (2) 같은 수를 여러 번 골라도 된다.

import sys

n,m = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))
array.sort()

def backtracking(arr, pre):
    if len(arr) == m:
        print(*arr, sep=" ")
        return
    pre = -1
    for i in range(n):
        if pre != array[i]:
            pre = array[i]
            backtracking(arr + [array[i]], pre)

backtracking([],-1)

# 3 1
# 4 4 2
# #
# 2
# 4

# 4 2
# 9 7 9 1
# #
# 1 1
# 1 7
# 1 9
# 7 1
# 7 7
# 7 9
# 9 1
# 9 7
# 9 9

# 4 4
# 1 1 2 2
# #
# 1 1 1 1
# 1 1 1 2
# 1 1 2 1
# 1 1 2 2
# 1 2 1 1
# 1 2 1 2
# 1 2 2 1
# 1 2 2 2
# 2 1 1 1
# 2 1 1 2
# 2 1 2 1
# 2 1 2 2
# 2 2 1 1
# 2 2 1 2
# 2 2 2 1
# 2 2 2 2