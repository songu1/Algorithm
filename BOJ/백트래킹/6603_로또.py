# 로또
# 독일 로또 {1,2,3,..49} 중 6개 고름
# 로또 선택 전략 : 49가지 수 중 k(k>6)개의 수를 골라 집합 s를 만들고 그 수를 가지고 번호를 선택
# k = 8 -> 28가지
# 집합 S과 k가 주어졌을 때 수를 고르는 모든 방법을 구하는 프로그램

# 입력 : 여러개의 테스트케이스, 각 테스트 케이스는 한줄
    # k(7~12), 집합S의 k개의 수(오름차순)
# 입력 마지막 줄 0
# 출력 : 각 테스트 케이스 마다 수를 고르는 모든 방법(사전순)
    # 각 테스트 케이스 사이에는 빈줄

# 조합 방법 - 더 빠름! 하지만 백트래킹 연습을 위해 2번 풀이 학습하기

import sys

# 순열 라이브러리 사용
# from itertools import *

# s=[]
# while True:
#     s=list(map(int,sys.stdin.readline().split()))
#     if s[0] == 0:
#         break
#     k = s[0]
#     del s[0]
#     lotto = list(combinations(s,6))
#     for i in range(len(lotto)):
#         for j in range(6):
#             print(lotto[i][j], end=" ")
#         print()
#     print()    

# dfs를 활용한 백트래킹
def backtracking(idx, arr):
    if len(arr) == 6:
        for i in range(6):
            print(arr[i],end=" ")
        print()
        return
    
    for i in range(idx, len(s)):
        backtracking(i+1, arr + [s[i]])

s=[]
while True:
    s=list(map(int,sys.stdin.readline().split()))
    if s[0] == 0:
        break
    k = s[0]
    del s[0]
    backtracking(0,[])
    print()



# 7 1 2 3 4 5 6 7
# 8 1 2 3 5 8 13 21 34
# 0
# #
# 1 2 3 4 5 6
# 1 2 3 4 5 7
# 1 2 3 4 6 7
# 1 2 3 5 6 7
# 1 2 4 5 6 7
# 1 3 4 5 6 7
# 2 3 4 5 6 7

# 1 2 3 5 8 13
# 1 2 3 5 8 21
# 1 2 3 5 8 34
# 1 2 3 5 13 21
# 1 2 3 5 13 34
# 1 2 3 5 21 34
# 1 2 3 8 13 21
# 1 2 3 8 13 34
# 1 2 3 8 21 34
# 1 2 3 13 21 34
# 1 2 5 8 13 21
# 1 2 5 8 13 34
# 1 2 5 8 21 34
# 1 2 5 13 21 34
# 1 2 8 13 21 34
# 1 3 5 8 13 21
# 1 3 5 8 13 34
# 1 3 5 8 21 34
# 1 3 5 13 21 34
# 1 3 8 13 21 34
# 1 5 8 13 21 34
# 2 3 5 8 13 21
# 2 3 5 8 13 34
# 2 3 5 8 21 34
# 2 3 5 13 21 34
# 2 3 8 13 21 34
# 2 5 8 13 21 34
# 3 5 8 13 21 34