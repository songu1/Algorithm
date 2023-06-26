# N과 M (10)
# (1) n개의 자연수 중 m개를 고른 수열
# (2) 고른 수열은 비내림차순 (a1 <= a2 <= ... <= ak)

import sys

n,m =map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))
array.sort()

def backtracking(idx, arr, pre):
    if len(arr) == m:
        print(*arr, sep=" ")
        return
    pre = -1
    for i in range(idx,n):
        if pre != array[i]:
            pre = array[i]
            backtracking(i+1,arr + [array[i]], pre)

backtracking(0,[],-1)

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
# 7 9
# 9 9

# 4 4
# 1 1 2 2
# #
# 1 1 2 2