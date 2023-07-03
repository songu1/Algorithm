# 떡 먹는 호랑이
# 어제 받은 떡의 개수 + 그저께 받은 떡의 개수를 더한만큼 떡을 받아야 할머니를 보내줌
# 오늘 호랑이에게 몇개의 떡을 줬는지(K개) , 떡을 준지 며칠되었는지(D째날)
# 처음 만난날에 준 떡의 개수 A, 그 다음날에 준 떡의 개수 B를 계산하는 프로그램
# 답이 되는 A,B가 1개이상이면 1개만 구해서 출력

# 입력 : 할머니가 넘어온날 D(3~30) , 그날 호랑이에게 준 떡의 개수 K(10~100,000)
# 출력 : 첫째날 준 떡의 개수 A
# 둘째날 준 떡의 개수 B (1 <= A <= B)


# 피보나치 수열 dp[i] = dp[i-1] + dp[i-2]

import sys

d,k = map(int,sys.stdin.readline().split())
dp = [[0,0] for _ in range(d+1)]    # dp[i][0] : A / dp[i][1] : B
dp[1] = [1,0]
dp[2] = [0,1]

for i in range(3,d+1):
    dp[i][0] = dp[i-2][0] + dp[i-1][0]
    dp[i][1] = dp[i-2][1] + dp[i-1][1]

# dp[d]번째 -> k
for a in range(1,k//sum(dp[d])+1):
    if (k-dp[d][0]*a) % dp[d][1] == 0:
        b = (k-dp[d][0]*a) // dp[d][1]
        print(a)
        print(b)
        break

# 6 41
# #
# 2
# 7

# 7 218
# #
# 10
# 21