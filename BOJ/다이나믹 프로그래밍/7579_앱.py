# 앱
# 새로운 앱을 실행 -> 활성화된 앱 중 몇개를 선택하여 메모리로부터 삭제 (비활성화)
# 비활성화된 앱들을 재실행하는 경우 그만큼 시간이 더 필요함
# n개의 앱 a1 ~ an이 활성화, ai는 mi바이트만큼 메모리 사용
# 비활성화 후 다시 실행할때 비용 ci
# 새로운 앱 b를 실행하여 추가로 m바이트의 메모리가 필요할때
    # 활성화된 앱 ai~an 중 몇개를 비활성화하여 m바이트 이상의 메모리를 확보
# 비활성화했을 경우의 비용 ci의 합을 최소화하여 메모리 m바이트를 확보

# 입력 : 앱의 개수 n(1~100), 필요한 추가 메모리 m(1~10^7)
# n개의 정수로 활성화되어있는 앱의 메모리 바이트수 m1~mn (1~10^7)
# n개의 정수로 각 앱을 비활성화했을 경우의 비용 c1~cn (100)
# 출력 : 필요한 m바이트를 확보하기 위한 앱 비활성화의 최소 비용

# 3차 시도 : dp[메모리]=비용 이 아닌 dp[비용]=메모리 로 구해보기!
    # 메모리를 인덱스로 하면 10^7 * 100 까지 늘어나므로 시간,메모리가 어마어마함
    # 비용을 인덱스로 하면 100*100 까지만 있음
    # 배낭 문제에서 dp배열을 설정할때 값에 따라 dp의 인덱스를 다르게 설정해야함!

import sys

n,m = map(int,sys.stdin.readline().split())
marr = [0] + list(map(int,sys.stdin.readline().split()))
carr = [0] + list(map(int,sys.stdin.readline().split()))

# msum = sum(marr)
csum = sum(carr)

dp = [[0]*(csum+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(csum+1):
        if j >= carr[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-carr[i]] + marr[i])
        else:
            dp[i][j] = dp[i-1][j]

for i in range(csum+1):
    if dp[-1][i] >= m:
        print(i)
        break

# 5 60
# 30 10 20 35 40
# 3 0 3 5 4           # 6



# 1차시도 : 메모리 초과
# dp = [[0]*(msum-m+1) for _ in range(n)]

# for j in range(msum-m+1):
#     if j >= marr[0]:
#         dp[0][j] = carr[0]

# for i in range(1,n):
#     mi = marr[i]        # 현재 i의 m값
#     for j in range(msum-m+1):
#         if j >= mi:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-mi]+carr[i])
#         else:
#             dp[i][j] = dp[i-1][j]
#     # print(dp[i])
# # print(*dp,sep="\n")

# print(csum - dp[-1][-1])

# 2차시도 : 시간초과
# dp = [0]*(msum-m+1)

# for j in range(msum-m+1):
#     if j >= marr[0]:
#         dp[j] = carr[0]

# for i in range(1,n):
#     mi = marr[i]        # 현재 i의 m값
#     for j in range(msum-m,mi-1,-1):
#         if j >= mi:
#             dp[j] = max(dp[j], dp[j-mi]+carr[i])

# print(csum - dp[-1])