# 주식
# 매일 3가지 중 1개의 행동을 함
    # 주식 하나를 삼
    # 원하는 만큼 가지고 있는 주식을 팜
    # 아무것도 안함
# 날 별로 주식의 가격 -> 최대 이익
# n=3일, 날 별 주가 [10,7,6] -> 주가가 감소하므로 최대 이익은 0
# n=3일, 날 별 주가 [3,5,9] -> 처음 두날 주식 사고 마지막날 팔면 이익이 10

# 입력 : 테스트 케이스 수 t
# 자연수 n(2~1000000)
# 날 별 주가를 나타내는 n개의 자연수가 공백으로(1~10000)
# 출력 : 각 테스트케이스 별로 최대 이익을 나타내는 정수 하나를 출력(부호있는 64bit 정수형)

# 1차시도 : 4% 시간 초과
# 2차시도 : 통과 - max값을 찾는 것을 O(n)으로 수행

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    cost = list(map(int,sys.stdin.readline().split()))
    maxlist = []
    maxCost = 0
    for i in range(n-1,-1,-1):
        if cost[i] > maxCost:
            maxlist.append(i)
            maxCost = cost[i]
    result = 0
    start = 0
    while start < n:
        idx = maxlist.pop()
        result += cost[idx]*(idx-start) - sum(cost[start:idx])
        start = idx + 1
    print(result)

# t = int(sys.stdin.readline())
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     cost = list(map(int,sys.stdin.readline().split()))
#     # 최대 이익 찾기
#     result = 0
#     start = 0
#     while start < n:
#         maxCost = 0
#         for i in range(start,n):
#             if maxCost < cost[i]:
#                 maxCost = cost[i]
#                 idx = i
#         result += cost[idx]*(idx-start) - sum(cost[start:idx])
#         start = idx+1
#     print(result)
    

# 5
# 3
# 10 7 6
# 3
# 3 5 9
# 5
# 1 1 3 1 2
# 6
# 4 2 9 3 8 1
# 8
# 3 2 8 5 7 4 2 9
# #
# 0
# 10
# 5
# 17
# 32