# N과 M (12)
# (1) N개의 자연수 중에서 M개를 고른 수열
# (2) 같은 수를 여러 번 골라도 된다.
# (3) 고른 수열은 비내림차순이어야 한다. (A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK)
# -> 중복 조합

import sys

n,m = map(int,sys.stdin.readline().split())
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
            backtracking(i,arr + [array[i]], pre)

backtracking(0,[],-1)


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
# 7 7
# 7 9
# 9 9

# 4 4
# 1 1 2 2
# #
# 1 1 1 1
# 1 1 1 2
# 1 1 2 2
# 1 2 2 2
# 2 2 2 2