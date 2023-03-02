# 병사 배치하기 -> LIS 알고리즘으로 풀어야 함 (풀이 참고)
# n명의 병사가 무작위로 나열되어있음
# 각 병사는 특정한 값의 전투력을 보유
# 전투력이 높은 병사가 앞쪽에 오도록 내림차순 배치 (앞쪽 병사의 전투력이 더 높아야함)
# 배치 과정에서 특정 위치의 병사 열외(정렬X), 남아있는 병사의 수 최대
# 병사에 대한 정보 -> 남아있는 병사의 수가 최대가 되도록하기위해 열외시켜야하는 병사의 수

# 입력 : n (1~2000)
# 각 병사의 전투력 (1~1000만)
# 출력 : 남아있는 병사의 수가 최대가 되도록 하기위해 열외시켜야하는 병사의 수

import sys

n=int(sys.stdin.readline())
fight=list(map(int,sys.stdin.readline().split()))
d=[1]*n

for i in range(1,n):
    for j in range(0,i):
        if fight[i]<fight[j]:
            d[i]=max(d[i],d[j]+1)

print(n-max(d))



# 7
# 15 11 4 8 5 2 4         # 2

# 12
# 12 2 5 3 2 10 8 7 15 5 4 3      # 5

# 1
# 1000000                 # 0

# 6
# 1 2 1 2 1 2             # 4

# 가장 긴 증가하는 부분 수열 (Longest Incresing Subsequence, LIS)
# D[i]=array[i]를 마지막 원소로 가지는 부분 수열의 최대길이
# 점화식
    # 모든 0<=j<i에 대하여 D[i]=max(D[i],D[j]+1) if array[j] < array[i]

# 이코테 코드
# n=int(input())
# array=list(map,input().split())
# # 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
# array.reverse()

# # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
# dp=[1]*n

# # 가장 긴 증가하는 부분 수열 알고리즘 수행
# for i in range(1,n):
#     for j in range(0,i):
#         if array[j]<array[i]:
#             dp[i] = max(dp[i],dp[j]+1)

# # 열외해야하는 병사의 최소 수
# print(n-max[dp])